from typing import List


class TrapRainwater:
    def get_max_rain_water(self, lst: List[int]) -> int:

        if not lst:
            return 0

        left, right = 0, len(lst) - 1
        left_max, right_max = lst[left], lst[right]
        result = 0
        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, lst[left])
                result += left_max - lst[left]

            else:
                right -= 1
                right_max = max(right_max, lst[right])
                result += right_max - lst[right]

        return result
