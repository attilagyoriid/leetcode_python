from typing import List


class DuplicatesInArray:

    @staticmethod
    def contains_duplicates(nums: List[int]) -> bool:
        """
        Checks if there is duplicate in input array
        :param nums: list of integers
        :type nums: List
        :return: true if there is duplicate in input array
        :rtype: boolean
        """
        if len(nums) <= 1:
            return False
        dictionary = {}
        for num in nums:
            if num in dictionary:
                return True
            dictionary[num] = True

        return False
