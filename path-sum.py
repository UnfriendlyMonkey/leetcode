# https://leetcode.com/problems/path-sum/submissions/960858727/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def recursive_adding(node, targetSum, sum):
            if not node:
                return False
            elif not node.right and not node.left:
                return sum + node.val == targetSum
            else:
                return (
                    recursive_adding(node.left, targetSum, sum + node.val)
                    or recursive_adding(node.right, targetSum, sum + node.val)
                )
        return recursive_adding(root, targetSum, sum)
