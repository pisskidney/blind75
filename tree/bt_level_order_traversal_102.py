from typing import Optional, List


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def go(node, level, res):
            if node is None:
                return

            if len(res) <= level:
                res.append([])

            res[level].append(node.val)

            go(node.left, level+1, res)
            go(node.right, level+1, res)

        res = []
        go(root, 0, res)
        return res
