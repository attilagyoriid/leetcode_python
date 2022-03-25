from leetcode_python.src.algorithms.tree.node import Node


class BalanceBinaryTree:

    def is_balanced(self, root: Node) -> bool:
        def dfs(current_root):
            if not current_root:
                return [True, 0]

            left, right = dfs(current_root.left), dfs(current_root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1] <= 1))
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
