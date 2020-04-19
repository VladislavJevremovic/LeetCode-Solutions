# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def heightAndDiameter(node):
            if not node:
                return (0, 0)
            
            h1, d1 = heightAndDiameter(node.left)
            h2, d2 = heightAndDiameter(node.right)
            
            return 1 + max(h1, h2), max(d1, d2, h1 + h2)
        
        return f(root)[1]