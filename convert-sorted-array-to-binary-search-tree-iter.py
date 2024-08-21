# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/960028387/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        m = len(nums) // 2
        root = TreeNode(nums[m], (0, m - 1), (m + 1, len(nums) - 1))
        stack = [root]

        while stack:
            node = stack.pop()
            l, r = node.left
            if l > r:
                node.left = None
            elif l == r:
                node.left = TreeNode(nums[l])
            else:
                m = (l + r) // 2
                node.left = TreeNode(nums[m], (l, m - 1), (m + 1, r))
                stack.append(node.left)
            l, r = node.right
            if l > r:
                node.right = None
            elif l == r:
                node.right = TreeNode(nums[l])
            else:
                m = (l + r) // 2
                node.right = TreeNode(nums[m], (l, m - 1), (m + 1, r))
                stack.append(node.right)

        return root
