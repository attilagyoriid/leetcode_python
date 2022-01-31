import unittest

from leetcode_python.src.algorithms.arrays.sliding_window_maximum import SlidingWindowMaximum


class TestSlidingWindowMaximum(unittest.TestCase):
    def test_calculate(self):
        sliding_window_maximum = SlidingWindowMaximum()
        l = [1, 3, -1, -3, 5, 3, 6, 7]
        result = sliding_window_maximum.calculate(l, 3)
        self.assertEqual(result, list([3, 3, 5, 5, 6, 7]))
