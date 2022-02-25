from leetcode_python.src.algorithms.tree.node import Node


class SubTreeOfAnother:

    def is_sub_tree(self, tree: Node, sub_tree: Node) -> bool:
        if not sub_tree:
            return True
        if not tree:
            return False
        if self.is_same(tree, sub_tree):
            return True
        return self.is_sub_tree(tree.left, sub_tree) or self.is_sub_tree(tree.right, sub_tree)

    def is_same(self, root_a: Node, root_b: Node) -> bool:

        if not root_a and not root_b:
            return True
        if (not root_a or not root_b) or root_a.value != root_b.value:
            return False

        return self.is_same(root_a.left, root_b.left) and self.is_same(root_a.right, root_b.right)
