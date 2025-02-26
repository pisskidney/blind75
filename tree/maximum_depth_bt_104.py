class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def go(node):
            return 0 if node is None else 1 + max(go(node.left), go(node.right))
        return go(root)
