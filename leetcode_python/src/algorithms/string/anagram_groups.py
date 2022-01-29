from collections import defaultdict
from typing import List


class AnagramGroups:
    def group(self, list_of_anagrams: List[str]) -> List[List[str]]:

        dictionary = defaultdict(list)

        for string in list_of_anagrams:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1

            dictionary[tuple(count)].append(string)

        return list(dictionary.values())
