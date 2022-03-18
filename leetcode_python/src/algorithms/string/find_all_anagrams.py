from typing import List


class FindAllAnagrams:

    def find(self, text: str, pattern: str) -> List[int]:
        current_pointer_character_map = {}
        pattern_character_map = {}

        for i in range(len(pattern)):
            pattern_character_map[pattern[i]] = pattern_character_map.get(pattern[i], 0) + 1
            current_pointer_character_map[text[i]] = current_pointer_character_map.get(text[i], 0) + 1
            print("")

        result = [0] if current_pointer_character_map == pattern_character_map else []

        left = 0
        for c in range(len(pattern), len(text)):
            current_pointer_character_map[text[c]] = current_pointer_character_map.get(text[c], 0) + 1
            current_pointer_character_map[text[left]] -= 1
            if current_pointer_character_map[text[left]] == 0:
                current_pointer_character_map.pop(text[left])
            left += 1
            if current_pointer_character_map == pattern_character_map:
                result.append(left)

        return result
