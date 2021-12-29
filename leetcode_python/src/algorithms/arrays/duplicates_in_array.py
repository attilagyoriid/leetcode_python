from typing import List


class DuplicatesInArray:

    @staticmethod
    def contains_duplicates(nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False;
        dictionary = {}
        for num in nums:
            if num in dictionary:
                return True;
            dictionary[num] = True

        return False
