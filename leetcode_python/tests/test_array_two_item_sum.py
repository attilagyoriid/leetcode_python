from unittest import TestCase

from leetcode_python.src.algorithms.arrays.array_two_item_sum import ArrayTwoItemsSum


class ArrayItemSum(TestCase):

    def test_find_two_items_to_sum_up_to_value_backing_array(self):
        self.assertTrue(ArrayTwoItemsSum.find_two_items_to_sum_up_to_value_with_backing_array([2, 4, 5, 9, 12], 21))

    def test_find_two_items_to_sum_up_to_value_backing_hashmap(self):
        self.assertTrue(ArrayTwoItemsSum.find_two_items_to_sum_up_to_value_with_backing_hashmap([2, 4, 5, 9, 12], 21))