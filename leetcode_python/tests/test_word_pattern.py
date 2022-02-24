import unittest

from leetcode_python.src.algorithms.string.word_pattern import WordPattern


class TestWordPattern(unittest.TestCase):

    def test_valid(self):

        pattern = WordPattern()
        self.assertTrue(pattern.valid("abba", "dog cat cat dog"))

    def test_valid_(self):

        pattern = WordPattern()
        self.assertFalse(pattern.valid("abca", "dog cat cat dog"))