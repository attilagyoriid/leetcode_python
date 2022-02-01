import unittest

from leetcode_python.src.algorithms.arrays.best_time_to_buy_and_sell_stocks import BestTimeToBuyAndSellStocks


class TestBestTimeToBuyAndSellStocks(unittest.TestCase):

    def test_calculate(self):
        stocks = BestTimeToBuyAndSellStocks()

        self.assertEqual(stocks.calculate([7, 1, 5, 3, 6, 4]), 5)

