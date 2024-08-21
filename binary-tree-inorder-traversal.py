# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: TreeNode) -> None:
            if node.left:
                traverse(node.left)
            result.append(node.val)
            if node.right:
                traverse(node.right)

        if root:
            traverse(root)
        return result
