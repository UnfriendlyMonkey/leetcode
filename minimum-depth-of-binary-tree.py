# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/962860301/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_depth = 100001

    def _min_depth(self, node, cur_depth=1):
        if not (node.left or node.right):
            self.min_depth = min(self.min_depth, cur_depth)
            return
        if node.left:
            self._min_depth(node.left, cur_depth + 1)
        if node.right:
            self._min_depth(node.right, cur_depth + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self._min_depth(root, 1)
        return self.min_depth
