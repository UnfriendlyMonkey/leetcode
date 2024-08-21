# https://leetcode.com/problems/invert-binary-tree/submissions/983281048/
# recursive is more efficient in this task
# https://leetcode.com/problems/invert-binary-tree/submissions/983289621/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            queue = deque()
            queue.append(root)

            while queue:
                node = queue.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)
        return root
