import unittest

from leetcode_python.src.algorithms.arrays.find_minimum_in_rotated_sorted_array import FindMinimumInRotatedSortedArray


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):

    def test_calculate(self):
        find_min = FindMinimumInRotatedSortedArray()

        self.assertEqual(find_min.calculate([3, 4, 5, 1, 2]), 1)
