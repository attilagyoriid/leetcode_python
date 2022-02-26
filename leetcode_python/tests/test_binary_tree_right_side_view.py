import unittest

from leetcode_python.src.algorithms.tree.binary_tree_right_side_view import BinaryTreeRightSideView
from leetcode_python.src.algorithms.tree.node import Node


class TestBinaryTreeRightSideView(unittest.TestCase):

    def test_get_right_side_view(self):
        view = BinaryTreeRightSideView()
        root = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        self.assertEqual(view.get_right_side_view(root), [2, 4, 13, 78, 11])
