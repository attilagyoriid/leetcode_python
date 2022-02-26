from collections import deque
from typing import List

from leetcode_python.src.algorithms.tree.node import Node


class BinaryTreeRightSideView:

    def get_right_side_view(self, root: Node) -> List[int]:
        result = []
        if not root:
            return result

        levels = deque()

        levels.append(root)

        while levels:
            size = len(levels)
            for i in range(size):
                current_node: Node = levels.popleft()
                if i == size - 1:
                    result.append(current_node.value)

                if current_node.left:
                    levels.append(current_node.left)
                if current_node.right:
                    levels.append(current_node.right)

        return result
