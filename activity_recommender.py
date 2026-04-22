"""
Activity recommender for the Mood Machine.

Uses Yelp Fusion API to find nearby activities based on the user's
detected mood and the 3-label system (positive, negative_relax, negative_cheerup).
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

# Maps 3-label mood to list of search terms for Yelp.
MOOD_TO_QUERY = {
    "positive":          ["restaurant", "cafe", "bar", "park", "entertainment"],
    "negative_relax":    ["yoga", "spa", "gym", "nature reserve", "library"],
    "negative_cheerup":  ["comedy club", "karaoke", "bowling", "arcade", "music venue"],
}

# Opening line printed before the activity list.
MOOD_FRAMING = {
    "positive":          "Wonderful! Here's how to keep the good vibes going:",
    "negative_relax":    "Here are some relaxing activities nearby to help you unwind:",
    "negative_cheerup":  "Here are some fun activities nearby to cheer you up:",
}


def get_activities(mood: str, location: str, limit: int = 5) -> list:
    """
    Query Yelp Fusion API for places matching the given mood near location.
    Searches across multiple activity types and combines results.

    Returns a list of dicts with keys: name, category, address, distance, latitude, longitude.
    Returns an empty list on any API error.
    """
    if not YELP_API_KEY:
        print("[activity_recommender] No YELP_API_KEY found in .env")
        return []

    queries = MOOD_TO_QUERY.get(mood, ["activities"])
    if isinstance(queries, str):
        queries = [queries]

    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}",
        "Accept": "application/json"
    }

    results = []
    for query in queries:
        params = {"location": location, "term": query, "limit": limit}
        try:
            resp = requests.get(YELP_SEARCH_URL, headers=headers, params=params, timeout=8)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            print(f"[Yelp] Error for '{query}': {e}")
            continue

        for business in data.get("businesses", []):
            results.append({
                "name":      business.get("name", "Unknown"),
                "category":  (business.get("categories") or [{}])[0].get("title", "Activity"),
                "address":   business.get("location", {}).get("address1", "N/A"),
                "distance":  business.get("distance", 0),
                "latitude":  business.get("coordinates", {}).get("latitude"),
                "longitude": business.get("coordinates", {}).get("longitude"),
            })

    return results


def format_response(mood: str, activities: list, user_location: str = None) -> str:
    """
    Build the final string to print to the user with Google Maps directions links.

    Args:
        mood: The detected mood.
        activities: List of activity dicts with coordinates.
        user_location: User's street address for generating directions links.
    """
    lines = [MOOD_FRAMING.get(mood, "Here are some activities nearby:"), ""]

    if not activities:
        lines.append("  (No results — check your API key and location.)")
        return "\n".join(lines)

    for i, act in enumerate(activities, 1):
        km = act["distance"] / 1000
        lines.append(f"  {i}. {act['name']} ({act['category']})")
        lines.append(f"     {act['address']}  —  {km:.1f} km away")

        if act.get("latitude") and act.get("longitude"):
            if user_location:
                maps_url = f"https://www.google.com/maps/dir/?api=1&origin={user_location.replace(' ', '+')}&destination={act['latitude']},{act['longitude']}&travelmode=driving"
            else:
                maps_url = f"https://www.google.com/maps/search/?api=1&query={act['name'].replace(' ', '+')}&center={act['latitude']},{act['longitude']}"
            lines.append(f"     🗺️  Directions: {maps_url}")
        lines.append("")

    return "\n".join(lines)
