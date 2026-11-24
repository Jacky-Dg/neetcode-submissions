# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def pathHelper(root: Optional[TreeNode]) -> int:
            if not root or (root.left == None and root.right == None):
                return 1

            return 1 + max(pathHelper(root.left), pathHelper(root.right))

        if not root or (root.left == None and root.right == None):
            return 1

        left = pathHelper(root.left) if root.left else 0
        right = pathHelper(root.right) if root.right else 0

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return max(left, right, right + left)