import collections
from typing import List

from leetcode_python.src.algorithms.tree.node import Node


class BreathFirstSearchTraversal:

    @staticmethod
    def traverse( root: Node) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                node = queue.popleft();
                if node:
                    level.append(node.value)
                    queue.append(node.left)
                    queue.append(node.right)
            result.append(level)
        return result
