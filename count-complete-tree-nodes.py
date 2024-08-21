# https://leetcode.com/problems/count-complete-tree-nodes/description/
# https://leetcode.com/problems/count-complete-tree-nodes/submissions/1332000005/
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://algo.monster/liteproblems/222
    def countNodes(self, root: TreeNode | None) -> int:
        def count_depth(node: TreeNode | None) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        if not root:
            return 0

        left_depth = count_depth(root.left)
        right_depth = count_depth(root.right)

        if left_depth == right_depth:
            # means that left subtree is complete
            # 2 ** left_depth is for all nodes in left subtree + root
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)


class Solution_1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        levels = 0
        leftmost = True
        # node = root
        # while node.left:
        #     levels += 1
        #     node = node.left
        nodes = [(root, leftmost)]
        while True:
            node = nodes.pop(0)
            leftmost = node[1]
            node = node[0]
            if leftmost:
                levels += 1
                if not node.left or not node.left.left:
                    break
            nodes.append((node.left, leftmost))
            nodes.append((node.right, False))

        base = 2 ** (levels + 1) - 1
        if not node.right:
            return base + 1
        left = 0
        right = len(nodes) - 1
        middle = 0
        while left < right:
            middle = (left + right) // 2
            node = nodes[middle][0]
            if not node.left:
                right = middle - 1
                continue
            if node.right:
                left = middle + 1
                continue
            break
        return base + middle * 2 + bool(node.left) + bool(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(8)
sol = Solution()
print(sol.countNodes(root))
