from typing import List


class FindPeak:

    def find(self, lst: List[int]) -> int:
        if not lst or len(lst) == 0:
            return 0

        left = 0
        right = len(lst) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if lst[mid] < lst[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
