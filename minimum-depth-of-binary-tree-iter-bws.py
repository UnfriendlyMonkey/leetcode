# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/962870112/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        min_depth, level_end = 1, root
        while queue:
            node = queue.pop(0)
            # starting from the left
            if not (node.left or node.right):
                break
                # no need to search the other part of the tree
                # - it couldn't be less deep
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node == level_end:
                # go to the next level after checking the rightmost node
                # of current level
                min_depth += 1
                level_end = node.right if node.right else node.left
                # the rightmost node of rightmost node of previous level
                # becomes new level end
        return min_depth
