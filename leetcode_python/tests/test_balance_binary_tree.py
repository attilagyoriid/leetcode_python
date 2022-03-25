import unittest

from leetcode_python.src.algorithms.tree.balance_binary_tree import BalanceBinaryTree
from leetcode_python.src.algorithms.tree.node import Node


class TestBalanceBinaryTree(unittest.TestCase):

    def test_is_balanced(self):
        balance_tree = BalanceBinaryTree()
        root = Node(2, Node(1, Node(4), Node(5)), Node(4, Node(8), Node(9)))
        self.assertTrue(balance_tree.is_balanced(root))

    def test_not_balanced(self):
        balance_tree = BalanceBinaryTree()
        root = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        self.assertFalse(balance_tree.is_balanced(root))