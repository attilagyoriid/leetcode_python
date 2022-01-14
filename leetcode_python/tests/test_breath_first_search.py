from leetcode_python.src.algorithms.tree.breath_first_search import BreathFirstSearchTraversal
from leetcode_python.src.algorithms.tree.node import Node


def test_traverse():
    root = Node(2, Node(1, Node(4, Node(9, Node(12), Node(19)))), Node(4, Node(13, Node(78, Node(98), Node(11)))))

    print(BreathFirstSearchTraversal.traverse(root))
    assert [[2], [1, 4], [4, 13], [9, 78], [12, 19, 98, 11]] == BreathFirstSearchTraversal.traverse(root)
