from typing import List


class CombinationSum:
    def get_combinations(self, lst: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            if index >= len(lst) or total > target:
                return

            current.append(lst[index])
            dfs(index, current, total + lst[index])
            current.pop()
            dfs(index + 1, current, total)

        dfs(0, [], 0)

        return result
