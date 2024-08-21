# https://leetcode.com/problems/binary-tree-paths/submissions/990360382/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        pool = [(root, str(root.val))]
        while pool:
            node, path = pool.pop(0)
            if not (node.left or node.right):
                result.append(path)
            if node.left:
                pool.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                pool.append((node.right, path + '->' + str(node.right.val)))
        return result
