# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the freshest one
            if node:
                if visited:  # all childrens allready added
                    result.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node, True))
                    stack.append((node.right, False))  # stack is reversed
                    stack.append((node.left, False))
        print(result)
        return result


n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3, left=n1, right=n2)
sol = Solution()
sol.postorderTraversal(n3)
