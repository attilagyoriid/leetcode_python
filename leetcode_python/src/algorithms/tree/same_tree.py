from leetcode_python.src.algorithms.tree.node import Node


class SameTree:
    def is_same(self, root_a: Node, root_b: Node) -> bool:

        if not root_a and not root_b:
            return True
        if (not root_a or not root_b) or root_a.value != root_b.value:
            return False

        return self.is_same(root_a.left, root_b.left) and self.is_same(root_a.right, root_b.right)
