import unittest

from leetcode_python.src.algorithms.arrays.product_of_array_except_self import ProductOfArrayExceptSelf


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_calculate(self):
        except_self = ProductOfArrayExceptSelf()

        self.assertEqual(except_self.calculate([1, 2, 3, 4]), [24, 12, 8, 6])
