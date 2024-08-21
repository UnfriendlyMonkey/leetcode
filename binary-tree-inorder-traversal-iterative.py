# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/713539/python-3-all-iterative-traversals-inorder-preorder-postorder-similar-solutions/?page=2

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the freshest one
            if node:
                if visited:  # all childrens allready added
                    result.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))  # stack is reversed
                    stack.append((node, True))
                    stack.append((node.left, False))
        return result
