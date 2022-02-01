from typing import List


class BestTimeToBuyAndSellStocks:

    def calculate(self, days_with_price: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(days_with_price):

            if days_with_price[right] > days_with_price[left]:
                max_profit = max(max_profit, days_with_price[right] - days_with_price[left])
            else:
                left = right
            right += 1

        return max_profit
