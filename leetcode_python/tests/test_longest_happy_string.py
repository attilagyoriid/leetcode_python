import unittest

from leetcode_python.src.algorithms.string.longest_happy_string import LongestHappyString


class TestLongestHappyString(unittest.TestCase):

    def test_get_longest_happy_string(self):
        self.assertEqual("ccaccbcc", LongestHappyString().get_longest_happy_string(1, 1, 7))
