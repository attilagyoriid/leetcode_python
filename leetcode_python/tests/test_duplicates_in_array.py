from unittest import TestCase

from leetcode_python.src.algorithms.arrays.duplicates_in_array import DuplicatesInArray


class TestArrayDuplicates(TestCase):

    def test_contains_duplicates_happy(self):
        nums = (1, 2, 3, 4, 2, 1)
        self.assertTrue(DuplicatesInArray.contains_duplicates(nums))

    def test_contains_duplicates_empty(self):
        nums = ()
        self.assertFalse(DuplicatesInArray.contains_duplicates(nums))

    def test_contains_duplicates_one_item(self):
        nums = (1,)
        self.assertFalse(DuplicatesInArray.contains_duplicates(nums))

    def test_contains_duplicates_failure(self):
        nums = (1, 2, 3, 4)
        self.assertFalse(DuplicatesInArray.contains_duplicates(nums))
