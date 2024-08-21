from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        max_depth = 0
        while queue:
            temp_queue = queue
            queue = []
            for node in temp_queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1
        return max_depth
