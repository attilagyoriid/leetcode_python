from leetcode_python.src.algorithms.linked_list.ListNode import ListNode


class IsPalindromeLinkedList:

    def is_palindrome(self, head: ListNode) -> bool:
        fast: ListNode = head
        slow: ListNode = head
        # find middle
        while fast and fast.next_node:
            fast = fast.next_node.next_node
            slow = slow.next_node

        # reverse second part
        previous = None
        while slow:
            next = slow.next_node
            slow.next_node = previous
            previous = slow
            slow = next

        left, right = head , previous
        while right:
            if left.value != right.value:
                return False
            right = right.next_node
            left = left.next_node

        return True