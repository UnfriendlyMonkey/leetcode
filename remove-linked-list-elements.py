# https://leetcode.com/problems/remove-linked-list-elements/submissions/978527940/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:
        if not head:
            return None
        while head and head.val == val:
            head = head.next

        node = head
        while node and node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next
            if node.next:
                node = node.next
        return head if head else None

    def removeElements2(self, head, val):
        # not mine
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next
