import unittest

from leetcode_python.src.algorithms.arrays.remove_duplicates_from_sorted_array import RemoveDuplicatesFromSortedArray


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):

    def test_compute(self):
        from_sorted_array = RemoveDuplicatesFromSortedArray()
        result = from_sorted_array.compute([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        self.assertEqual(result, 5)