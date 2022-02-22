import unittest

from leetcode_python.src.algorithms.string.word_break import WordBreak


class TestWordBreak(unittest.TestCase):
    def test_can_break(self):
        word_break = WordBreak()

        self.assertTrue(word_break.can_break("leetcode", ["leet", "will", "code"]))
