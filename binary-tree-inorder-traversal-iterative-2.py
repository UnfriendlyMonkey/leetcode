# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/950456967/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        node = root
        nodes = []
        while node or nodes:
            if node:
                nodes.append(node)
                node = node.left
            else:
                node = nodes.pop()
                res.append(node.val)
                node = node.right
        return res
