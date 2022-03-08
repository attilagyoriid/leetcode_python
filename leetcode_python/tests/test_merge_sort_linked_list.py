import unittest

from leetcode_python.src.algorithms.linked_list.ListNode import ListNode
from leetcode_python.src.algorithms.linked_list.merge_sort_linked_list import MergeSortLinkedList


class TestMergeSortLinkedList(unittest.TestCase):

    def test_sort_list(self):
        head = ListNode(5)
        node2 = ListNode(4)
        node3 = ListNode(3)
        node4 = ListNode(8)
        node5 = ListNode(7)
        node4.next_node = node5
        node3.next_node = node4
        node2.next_node = node3
        head.next_node = node2

        result = MergeSortLinkedList().sort_list(head)
        result_list = []
        while result:
            result_list.append(result.value)
            result = result.next_node

        self.assertEqual(result_list, [3, 4, 5, 7, 8])
