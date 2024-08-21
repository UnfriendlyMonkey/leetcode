# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/967455173/
# not my idea
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            # they would equalize their length by this change
            # and meet either at intersection or at None
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
