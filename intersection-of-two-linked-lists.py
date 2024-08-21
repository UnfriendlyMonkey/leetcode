# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/967428650/

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
        passed = {}
        while headA or headB:
            if headA:
                if headA in passed:
                    return headA
                else:
                    passed[headA] = 1
                    headA = headA.next
            if headB:
                if headB in passed:
                    return headB
                else:
                    passed[headB] = 1
                    headB = headB.next
        return None
