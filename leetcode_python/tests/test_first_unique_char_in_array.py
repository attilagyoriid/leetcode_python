from unittest import TestCase

from leetcode_python.src.algorithms.string.first_unique_char_in_string import FirstUniqueCharInString


class TestFirstUniqueCharInArray(TestCase):

    def test_first_unique_char(self):
        word = "abcdabcdeff"
        self.assertEqual(FirstUniqueCharInString.first_unique_char(word), 8)

    def test_first_unique_char_one_char(self):
        word = "a"
        self.assertEqual(FirstUniqueCharInString.first_unique_char(word), 0)

    def test_first_unique_char_empty(self):
        word = ""
        self.assertEqual(FirstUniqueCharInString.first_unique_char(word), -1)

    def test_first_unique_char_no_unique(self):
        word = "abcdabcd"
        self.assertEqual(FirstUniqueCharInString.first_unique_char(word), -1)
