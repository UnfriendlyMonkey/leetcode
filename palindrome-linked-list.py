# https://leetcode.com/problems/palindrome-linked-list/submissions/986466868/

from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dd = deque([], maxlen=100000)
        while head:
            dd.append(head.val)
            head = head.next
        while len(dd) > 1:
            if dd.pop() != dd.popleft():
                return False
        return True

class Solution:
    def isPalindrome2(self, head) -> bool:
        self.left = ListNode(0, head)

        def recursiveFunc(head):
            if not head:
                return True

            right = recursiveFunc(head.next)
            self.left = self.left.next
            # at the deepest recursion 'left' steps on the first node
            # and 'head' is the last node
            # then 'left' moves on while 'head' recursively moves backwards
            return right and self.left.val == head.val
        return recursiveFunc(head)

    def isPalindrome3(self, head) -> bool:

        slow = fast = head
        while fast and fast.next:
            # find the middle of the list
            slow = slow.next
            fast = fast.next.next

        rev = None
        while slow:
            # reverse the second half of the list
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp

        while rev:
            # compare first half with reversed second
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next

        return True
