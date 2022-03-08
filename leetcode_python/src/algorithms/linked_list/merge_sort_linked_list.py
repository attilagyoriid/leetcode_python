from leetcode_python.src.algorithms.linked_list.ListNode import ListNode


class MergeSortLinkedList:

    def sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next_node:
            return head

        left = head
        right = self.get_middle(head)
        tmp = right.next_node
        right.next_node = None
        right = tmp

        left = self.sort_list(left)
        right = self.sort_list(right)

        return self.merge(left, right)

    def get_middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next_node

        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

        return slow

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:

        tail = dummy = ListNode()
        while list1 and list2:
            if list1.value < list2.value:
                tail.next_node = list1
                list1 = list1.next_node
            else:
                tail.next_node = list2
                list2 = list2.next_node

            tail = tail.next_node

        if list1:
            tail.next_node = list1
        if list2:
            tail.next_node = list2

        return dummy.next_node
