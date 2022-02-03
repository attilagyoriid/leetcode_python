from typing import List


class MaximumProductSubArray:

    def calculate(self, items: List[int]) -> int:
        result = max(items)
        maximum, minimum = 1, 1

        for i in items:

            if i == 0:
                maximum = 1
                minimum = 1
                continue
            temp_max = i*maximum
            maximum = max(i * minimum, temp_max, i)
            minimum = min(i * minimum, temp_max, i)

            result = max(result, maximum)

        return result




