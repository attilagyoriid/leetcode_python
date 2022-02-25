import unittest

from leetcode_python.src.algorithms.tree.node import Node
from leetcode_python.src.algorithms.tree.same_tree import SameTree
from leetcode_python.src.algorithms.tree.sub_tree_of_another_tree import SubTreeOfAnother


class TestSubTreeOfAnother(unittest.TestCase):

    def test_is_subtree(self):
        node1 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        node2 = Node(4, Node(9, Node(12), Node(19)))
        self.assertTrue(SubTreeOfAnother().is_sub_tree(node1, node2))

    def test_is_subtree_failure1 (self):
        node1 = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        node2 = Node(4, Node(9, Node(11), Node(19)))
        self.assertFalse(SubTreeOfAnother().is_sub_tree(node1, node2))
