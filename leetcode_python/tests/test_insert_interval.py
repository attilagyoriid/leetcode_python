import unittest

from leetcode_python.src.algorithms.arrays.insert_interval import InsertInterval


class TestInsertInterval(unittest.TestCase):

    def test_insert(self):
        interval = InsertInterval()
        self.assertEqual(interval.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
                         [[1, 2], [3, 10], [12, 16]])
