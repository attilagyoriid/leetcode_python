import unittest

from leetcode_python.src.algorithms.arrays.remove_covered_intervals import RemoveCoveredIntervals


class TestRemoveCoveredIntervals(unittest.TestCase):

    def test_get_intervals(self):
        self.assertEqual(RemoveCoveredIntervals().get_intervals([[1, 4], [3, 6], [2, 8]]), 2)
