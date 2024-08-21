# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/967433263/
# beats 88% in speed and 68% in memory

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
        while headA or headB:
            if headA:
                if hasattr(headA, 'passed'):
                    return headA
                else:
                    headA.passed = 1
                    headA = headA.next
            if headB:
                if hasattr(headB, 'passed'):
                    return headB
                else:
                    headB.passed = 1
                    headB = headB.next
        return None
