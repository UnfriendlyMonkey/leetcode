# https://leetcode.com/problems/reverse-linked-list/submissions/980314230/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            head.next, dummy, head = dummy, head, head.next
        return dummy
