"""
Unit tests for the Mood Machine classifiers.
Run with: python -m unittest tests -v
Or: python tests.py
"""

import unittest
from mood_analyzer import MoodAnalyzer


class TestMoodAnalyzer(unittest.TestCase):
    """Test the rule-based mood classifier."""

    def setUp(self):
        """Initialize the analyzer for each test."""
        self.analyzer = MoodAnalyzer()

    # Basic mood detection tests
    def test_happy_mood(self):
        """Test happy mood detection."""
        result = self.analyzer.detect_specific_mood("I feel amazing today")
        self.assertEqual(result, "happy")

    def test_stressed_mood(self):
        """Test stressed mood detection."""
        result = self.analyzer.detect_specific_mood("I am overwhelmed and anxious")
        self.assertEqual(result, "stressed")

    def test_sad_mood(self):
        """Test sad mood detection."""
        result = self.analyzer.detect_specific_mood("I feel so lonely and empty")
        self.assertEqual(result, "sad")

    def test_bored_mood(self):
        """Test bored mood detection."""
        result = self.analyzer.detect_specific_mood("I'm just scrolling, nothing to do")
        self.assertEqual(result, "bored")

    def test_angry_mood(self):
        """Test angry mood detection."""
        result = self.analyzer.detect_specific_mood("I'm so frustrated and livid")
        self.assertEqual(result, "angry")

    # Negation handling tests
    def test_negation_not_happy(self):
        """Test that negation prevents happy classification."""
        result = self.analyzer.detect_specific_mood("I'm not happy at all")
        self.assertNotEqual(result, "happy")

    def test_negation_not_sad(self):
        """Test that negation prevents sad classification when negation precedes keyword."""
        # The negation handling only skips a word if preceded directly by negation word
        result = self.analyzer.detect_specific_mood("not sad")
        self.assertNotEqual(result, "sad")

    def test_negation_handling_stressed(self):
        """Test negation before stressed mood word."""
        result = self.analyzer.detect_specific_mood("I'm not stressed about anything")
        self.assertNotEqual(result, "stressed")

    # Edge cases
    def test_empty_string(self):
        """Test that empty string returns a valid mood."""
        result = self.analyzer.detect_specific_mood("")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_returns_string(self):
        """Test that result is always a string."""
        result = self.analyzer.detect_specific_mood("feeling okay")
        self.assertIsInstance(result, str)

    def test_result_is_valid_mood(self):
        """Test that result is one of the five valid moods."""
        valid_moods = {"happy", "sad", "angry", "stressed", "bored"}
        result = self.analyzer.detect_specific_mood("I feel great")
        self.assertIn(result, valid_moods)

    def test_multiple_mood_words_happy(self):
        """Test detection with multiple happy keywords."""
        result = self.analyzer.detect_specific_mood("I'm so happy, excited, and joyful today")
        self.assertEqual(result, "happy")

    def test_multiple_mood_words_stressed(self):
        """Test detection with multiple stressed keywords."""
        result = self.analyzer.detect_specific_mood("I'm overwhelmed, anxious, and stressed out")
        self.assertEqual(result, "stressed")

    # Negation with multiple words
    def test_double_negation(self):
        """Test handling of double negation."""
        result = self.analyzer.detect_specific_mood("I'm not unhappy")
        self.assertIsNotNone(result)

    # Case insensitivity
    def test_case_insensitive_happy(self):
        """Test that detection is case-insensitive."""
        result1 = self.analyzer.detect_specific_mood("I FEEL HAPPY")
        result2 = self.analyzer.detect_specific_mood("I feel happy")
        self.assertEqual(result1, result2)

    def test_case_insensitive_sad(self):
        """Test sad detection is case-insensitive."""
        result = self.analyzer.detect_specific_mood("I FEEL SAD AND LONELY")
        self.assertEqual(result, "sad")

    # Preprocessing tests
    def test_whitespace_handling(self):
        """Test that extra whitespace is handled correctly."""
        result = self.analyzer.detect_specific_mood("  I  feel   happy  ")
        self.assertEqual(result, "happy")


class TestMoodAnalyzerEdgeCases(unittest.TestCase):
    """Test edge cases and robustness of the mood classifier."""

    def setUp(self):
        """Initialize the analyzer for each test."""
        self.analyzer = MoodAnalyzer()

    def test_single_word_mood(self):
        """Test detection with a single mood word."""
        result = self.analyzer.detect_specific_mood("happy")
        self.assertEqual(result, "happy")

    def test_mixed_emotions_defaults(self):
        """Test that mixed or unclear input returns a valid mood."""
        result = self.analyzer.detect_specific_mood("the quick brown fox jumps over the lazy dog")
        self.assertIsInstance(result, str)
        self.assertIn(result, {"happy", "sad", "angry", "stressed", "bored"})

    def test_negation_word_alone(self):
        """Test negation word without mood word."""
        result = self.analyzer.detect_specific_mood("not not not")
        self.assertIsInstance(result, str)

    def test_very_long_text(self):
        """Test with a very long input text."""
        long_text = "happy " * 100
        result = self.analyzer.detect_specific_mood(long_text)
        self.assertEqual(result, "happy")

    def test_special_characters(self):
        """Test that special characters don't break detection."""
        result = self.analyzer.detect_specific_mood("I am so happy!!! excited")
        self.assertEqual(result, "happy")


if __name__ == "__main__":
    unittest.main(verbosity=2)
