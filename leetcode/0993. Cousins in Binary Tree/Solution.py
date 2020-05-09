# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def depthAndParentValue(root: TreeNode, x: int, depth: int, parent: int) -> (int, int):
            if not root:
                return None
            
            if root.val == x:
                return (depth, parent)
            
            l = depthAndParentValue(root.left, x, depth + 1, root.val)
            r = depthAndParentValue(root.right, x, depth + 1, root.val)
            
            return l if l else r
        
        (x_depth, x_parent_value) = depthAndParentValue(root, x, 0, 0)
        (y_depth, y_parent_value) = depthAndParentValue(root, y, 0, 0)
        
        return x_depth == y_depth and x_parent_value != y_parent_value