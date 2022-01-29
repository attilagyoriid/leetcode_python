import unittest

from leetcode_python.src.algorithms.string.anagram_groups import AnagramGroups


class TestAnagramGroups(unittest.TestCase):

    def test_AnagramGroups(self):
        anagram_groups = AnagramGroups()
        result = anagram_groups.group(["abcd", "eeff", "ab", "ffee", "dcab", "efef", "ba", "bb"])
        for l in result:
            l.sort()
        result.sort()
        self.assertListEqual([['ab', 'ba'], ['abcd', 'dcab'], ['bb'], ['eeff', 'efef', 'ffee']], result)


