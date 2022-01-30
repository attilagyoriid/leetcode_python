class LongestSubstringWithoutRepeatingCharacters:
    def compute(self, text: str) -> int:
        left = 0
        maximum = 0
        characters_visited = set()

        for right in range(len(text)):
            while text[right] in characters_visited:
                characters_visited.remove(text[left])
                left += 1
            characters_visited.add(text[right])
            maximum = max(right-left + 1, maximum)

        return maximum
