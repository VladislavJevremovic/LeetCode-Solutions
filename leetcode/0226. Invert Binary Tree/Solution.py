# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root is None:
    #         return None

    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)
        
    #     root.left = right
    #     root.right = left
        
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
	    
	    queue = []
	    queue.append(root)
	    while queue:
	        current = queue.pop()
	        temp = current.left
	        current.left = current.right
	        current.right = temp
	        
	        if current.left:
	        	queue.append(current.left)
	        if current.right:
	        	queue.append(current.right)
	    
	    return root