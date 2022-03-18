import unittest

from leetcode_python.src.algorithms.string.find_all_anagrams import FindAllAnagrams


class TestFindAllAnagrams(unittest.TestCase):

    def test_find(self):
        self.assertEqual([0, 6, 15],FindAllAnagrams().find("adcdefcadaseacfdac", "acd"))

