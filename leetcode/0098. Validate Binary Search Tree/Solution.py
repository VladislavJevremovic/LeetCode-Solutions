# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTInRange(self, root: TreeNode, a: float, b: float) -> bool:
        if not root:
            return True

        if root.val <= a or root.val >= b:
            return False

        return self.isValidBSTInRange(root.left, a, root.val) and self.isValidBSTInRange(root.right, root.val, b)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTInRange(root, -float("inf"), float("inf"))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isNodeInRange(root: TreeNode, a: int, b: int) -> bool:
            if not root:
                return True
            
            if a >= root.val or root.val >= b:
                return False
            
            return isNodeInRange(root.left, a, root.val) and isNodeInRange(root.right, root.val, b)
            
        return isNodeInRange(root, -math.inf, math.inf)