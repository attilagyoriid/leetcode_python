from typing import List


class FindMinimumInRotatedSortedArray:

    def calculate(self, items: List[int]) -> int:

        result = items[0]
        left, right = 0, len(items) - 1

        while left <= right:

            if items[left] < items[right]:
                return min(result, items[left])

            middle = (right + left) // 2
            result = min(result, items[middle])
            if items[left] <= items[middle]:
                left = middle + 1
            else:
                right = right - 1
        return middle
