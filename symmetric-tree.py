# https://leetcode.com/problems/symmetric-tree/submissions/959114492/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right

        def _isSymmetric(p, q):
            if not p and not q:
                return True
            if not q or not p or (p.val != q.val):
                return False
            return (
                _isSymmetric(p.left, q.right)
                and _isSymmetric(p.right, q.left))
        return _isSymmetric(p, q)
