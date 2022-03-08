import unittest

from leetcode_python.src.algorithms.linked_list.ListNode import ListNode
from leetcode_python.src.algorithms.linked_list.is_palindrome_linked_list import IsPalindromeLinkedList


class TestIsPalindromeLinkedList(unittest.TestCase):

    def test_is_palindrome(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(2)
        node5 = ListNode(1)
        node4.next_node = node5
        node3.next_node = node4
        node2.next_node = node3
        head.next_node = node2

        self.assertTrue(IsPalindromeLinkedList().is_palindrome(head))
