from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def go(node):

            if not node:
                return float('-inf'), float('-inf')

            left_best_open, left_best_closed = go(node.left)
            right_best_open, right_best_closed = go(node.right)

            return [
                max(
                    node.val,
                    node.val + left_best_open,
                    node.val + right_best_open
                ),
                max(
                    left_best_closed,
                    right_best_closed,
                    node.val + left_best_open + right_best_open,
                    left_best_open,
                    right_best_open
                )
            ]

        return max(go(root))
