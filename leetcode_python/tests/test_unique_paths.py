import unittest

from leetcode_python.src.algorithms.arrays.unique_paths import UniquePaths


class TestUniquePaths(unittest.TestCase):

    def test_get_number_of_unique_paths(self):
        self.assertEqual(UniquePaths().get_number_of_unique_paths(7, 3), 28)

