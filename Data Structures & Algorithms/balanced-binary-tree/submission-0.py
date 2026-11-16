# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDiff = 0
        def heightHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = heightHelper(root.left)
            right = heightHelper(root.right)

            self.maxDiff = max(self.maxDiff, abs(left - right))

            return 1 + max(left, right)

        heightHelper(root)

        return self.maxDiff < 2