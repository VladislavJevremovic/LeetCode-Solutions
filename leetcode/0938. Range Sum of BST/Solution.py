# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        sum = 0
        sum += self.rangeSumBST(root.left, L, R)
        if L <= root.val and root.val <= R:
            sum += root.val
        sum += self.rangeSumBST(root.right, L, R)

        return sum

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:    
        sum = 0
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    sum += node.val
                
                if L < node.val:
                    stack.append(node.left)
                
                if node.val < R:
                    stack.append(node.right)
        
        return sum
