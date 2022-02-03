import unittest

from leetcode_python.src.algorithms.arrays.maximum_product_subarray import MaximumProductSubArray


class TestMaximumProductSubArray(unittest.TestCase):

    def test_calculate(self):
        max_prod_subarray = MaximumProductSubArray()

        self.assertEqual(24, max_prod_subarray.calculate([-1, -2, -3, -4]))

    def test_calculate_with_zero(self):
        max_prod_subarray = MaximumProductSubArray()

        self.assertEqual(12, max_prod_subarray.calculate([-1, -2, 0, -1, -3, -4]))

    def test_calculate_with_zero_end(self):
        max_prod_subarray = MaximumProductSubArray()

        self.assertEqual(12, max_prod_subarray.calculate([-1, -2, 0, -1, -3, -4, 0]))