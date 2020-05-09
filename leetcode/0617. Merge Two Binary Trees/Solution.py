# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            tmp = TreeNode(t1.val + t2.val)
            tmp.left = self.mergeTrees(t1.left, t2.left)
            tmp.right = self.mergeTrees(t1.right, t2.right)
            
            return tmp