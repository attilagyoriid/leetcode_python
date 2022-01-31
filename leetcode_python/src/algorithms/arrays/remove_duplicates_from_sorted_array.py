from typing import List


class RemoveDuplicatesFromSortedArray:
    def compute(self, items: List[int]) -> int:
        left = 1

        for right in range(1, len(items)):
            if items[right] != items[right - 1]:
                items[left] = items[right]
                left += 1
        return left
