import unittest

from leetcode_python.src.algorithms.tree.maximum_depth import MaximumDepth
from leetcode_python.src.algorithms.tree.node import Node


class TestMaximumDepth(unittest.TestCase):

    def test_max_depth(self):
        root = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))
        depth = MaximumDepth()
        self.assertEqual(depth.max_depth(root), 5)
