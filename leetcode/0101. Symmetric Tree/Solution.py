# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrored(root, root)
    
    def isMirrored(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2: # here at least 1 not None
            return False
        
        return t1.val == t2.val and self.isMirrored(t1.right, t2.left) and self.isMirrored(t1.left, t2.right)