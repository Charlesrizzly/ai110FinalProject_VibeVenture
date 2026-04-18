"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "This is beautiful",
    "This place is so nice",
    "Feeling like the best version of myself",
    "Feeling down today",
    "I'm a bit anxious",
    "What a horrible day",
    "No negativity, just good vibes",
    "I don't know how I'm feeling today",
    "I think I'm feeling good",
    "I'm either really anxious or really excited 🫠",
    "This is exhilarating",
    "I feel nothing 🫩",
    "What a wonderfully trashy day",
    "I could say I'm feeling good but I'd be lying",
    "Is any day not a good day ",
    "It's aight",
    "I am really happy",
    "I am sad",
    "I am not good",
    "I am not in a bad mood",
    "I am really angry right now",

]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive", # "This is beautiful"
    "positive", #  "This place is so nice"
    "positive", # "Feeling like the best version of myself"
    "negative", #  "Feeling down today"
    "negative", # "I'm a bit anxious"
    "negative", # "What a horrible day"
    "positive", # "No negativity, just good vibes"
    "mixed", # "I don't know how I'm feeling today"
    "positive", # "I think I'm feeling good"
    "mixed", # "I'm either really anxious or really excited 🫠"
    "positive", # "This is exhilarating"
    "negative", # "I feel nothing 🫩"
    "negative", # "What a  wonderfully trashy day"
    "negative", # "I could say I'm feeling good but I'd be lying"
    "positive", # "Is any day not a good day"
    "neutral", # "It's aight"
    "positive", # "I'm really happy"
    "negative", # "I am sad"
    "negative", # "I am not good"
    "positive", # "I am not in a bad mood"
    "negative", # "I am really angry right now"
    

]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
