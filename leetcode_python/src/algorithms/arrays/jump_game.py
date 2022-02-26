from typing import List


class JumpGame:

    def can_reach_last_index(self, lst: List[int]) -> bool:
        goal = len(lst) - 1

        for i in range(len(lst) - 1, -1, -1):
            if lst[i] + i >= goal:
                goal = i

        return goal == 0

