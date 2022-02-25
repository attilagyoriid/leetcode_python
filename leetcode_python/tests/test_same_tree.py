import unittest

from leetcode_python.src.algorithms.tree.node import Node
from leetcode_python.src.algorithms.tree.same_tree import SameTree


class TestSameTree(unittest.TestCase):

    def test_is_same(self):
        node1 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        node2 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        self.assertTrue(SameTree().is_same(node1, node2))

    def test_is_failure1 (self):
        node1 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        node2 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(97), Node(11)))))
        self.assertFalse(SameTree().is_same(node1, node2))
    def test_is_failure2 (self):
        node1 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        node2 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), ))))
        self.assertFalse(SameTree().is_same(node1, node2))