import unittest

from leetcode_python.src.algorithms.arrays.find_peak import FindPeak


class TestFindPeak(unittest.TestCase):

    def test_find(self):
        self.assertEqual(FindPeak().find([1, 2, 1, 3, 5, 6, 4]), 5)
