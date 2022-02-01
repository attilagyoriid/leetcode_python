from typing import List


class ProductOfArrayExceptSelf:

    def calculate(self, items: List[int]) -> List[int]:

        prefix = 1;
        result = [1] * len(items)

        for i in range(len(items)):
            result[i] = prefix
            prefix *= items[i]
        postfix = 1
        for i in range(len(items) - 1, -1, -1):
            result[i] *= postfix
            postfix *= items[i]

        return result
