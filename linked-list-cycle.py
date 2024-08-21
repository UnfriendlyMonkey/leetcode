# https://leetcode.com/problems/linked-list-cycle/submissions/966730003/
# better in speed
# https://leetcode.com/problems/linked-list-cycle/submissions/966734931/
# better in memory

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        # passed = {}
        while node:
            # if node in passed:
            if node.val is True:
                return True
            # passed[node] = 1
            node.val = True
            node = node.next
        return False
