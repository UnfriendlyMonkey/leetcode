# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/959366820/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def count_max_depth(node, current_depth):
            if not node:
                if current_depth > self.max_depth:
                    self.max_depth = current_depth
                return
            current_depth += 1
            count_max_depth(node.left, current_depth)
            count_max_depth(node.right, current_depth)
        count_max_depth(root, 0)
        return self.max_depth
