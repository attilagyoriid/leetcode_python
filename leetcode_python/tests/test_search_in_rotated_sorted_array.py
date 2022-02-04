import unittest

from leetcode_python.src.algorithms.arrays.search_in_rotated_sorted_array import SearchInRotatedSortedArray


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_calculate(self):
        search_array = SearchInRotatedSortedArray()
        self.assertEqual(search_array.calculate([4, 5, 6, 7, 0, 1, 2], 0), 4)
