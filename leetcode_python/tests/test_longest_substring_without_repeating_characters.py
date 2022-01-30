import unittest

from leetcode_python.src.algorithms.string.longest_substring_without_repeating_characters import \
    LongestSubstringWithoutRepeatingCharacters


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):

    def test_compute(self):
        lswrc = LongestSubstringWithoutRepeatingCharacters()
        result = lswrc.compute("adcdcfghjkfloktaimld")
        self.assertEqual(result, 8)
