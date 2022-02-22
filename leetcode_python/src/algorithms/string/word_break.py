from typing import List


class WordBreak:

    def can_break(self, string: str, word_dictionary: List[str]) -> bool:
        hits = [False] * (len(string) + 1)
        hits[len(string)] = True

        for i in range(len(string) - 1, -1, -1):
            for word in word_dictionary:
                if (i + len(word)) <= len(string) and word == string[i:i + len(word)]:
                    hits[i] = hits[i + len(word)]
                if hits[i]:
                    break
        return hits[0]
