# https://leetcode.com/problems/sum-of-left-leaves/
# https://leetcode.com/problems/sum-of-left-leaves/submissions/1325456751/
# https://leetcode.com/problems/sum-of-left-leaves/submissions/1325469268/
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recursiveSum(node: TreeNode, is_left: bool) -> int:
            if not (node.left or node.right):
                return node.val if is_left else 0
            sum = 0
            if node.left:
                sum += recursiveSum(node.left, is_left=True)
            if node.right:
                sum += recursiveSum(node.right, is_left=False)
            return sum

        if not root:
            return 0
        return recursiveSum(root, is_left=False)

    def sumOfLeftLeaves2(self, root: TreeNode | None) -> int:
        def recursiveSum(node: TreeNode | None) -> int:
            if not node:
                return 0
            sum = 0
            if node.left and not node.left.left and not node.left.right:
                sum += node.left.val
            sum += recursiveSum(node.left)
            sum += recursiveSum(node.right)
            return sum

        return recursiveSum(root)

    def sumOfLeftLeaves3(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        sum = 0
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val
        sum += self.sumOfLeftLeaves3(root.left)
        sum += self.sumOfLeftLeaves3(root.right)
        return sum
