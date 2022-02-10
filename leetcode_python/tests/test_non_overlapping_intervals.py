import unittest

from leetcode_python.src.algorithms.arrays.non_overlapping_intervals import NonOverlappingIntervals


class TestNonOverlappingIntervals(unittest.TestCase):

    def test_calculate(self):
        intervals = NonOverlappingIntervals()
        self.assertEqual(intervals.calculate([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
