# https://leetcode.com/problems/balanced-binary-tree/submissions/962246929/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_depth(node, cur_depth=0):
            if not node:
                return True, cur_depth
            cur_depth += 1
            is_left_balanced, depth_left = find_depth(node.left, cur_depth)
            if not is_left_balanced:
                return False, cur_depth
            is_right_balanced, depth_right = find_depth(node.right, cur_depth)
            if not is_right_balanced or abs(depth_left - depth_right) > 1:
                return False, cur_depth
            node_depth = max(depth_left, depth_right)
            return True, node_depth
        return find_depth(root, 0)[0]
