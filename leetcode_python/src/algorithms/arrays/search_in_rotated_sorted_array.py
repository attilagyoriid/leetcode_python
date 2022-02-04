from typing import List


class SearchInRotatedSortedArray:
    def calculate(self, items: List[int], to_search_for: int) -> int:
        left, right = 0, len(items) - 1

        while left <= right:
            middle = (left + right) // 2
            if items[middle] == to_search_for:
                return middle

            if items[left] <= items[middle]:

                if items[left] > to_search_for or items[middle] < to_search_for:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if items[right] < to_search_for or to_search_for < items[middle]:
                    right = middle - 1
                else:
                    left = left + 1

        return -1
