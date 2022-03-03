import unittest

from leetcode_python.src.algorithms.arrays.combination_sum import CombinationSum


class TestCombinationSum(unittest.TestCase):

    def test_get_combinations(self):
        self.assertEqual(CombinationSum().get_combinations([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
