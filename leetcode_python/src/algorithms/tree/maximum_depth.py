from leetcode_python.src.algorithms.tree.node import Node


class MaximumDepth:

    def max_depth(self, root: Node):
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        return max(left, right) + 1

