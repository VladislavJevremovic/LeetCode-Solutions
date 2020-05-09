# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        size = len(preorder)
        if not preorder or not size:
            return None

        stack = []
        
        i = 0
        root = TreeNode(preorder[i])
        stack.append(root)
        i += 1

        while i < size:
            temp = None
            while len(stack) and preorder[i] > stack[-1].val:
                temp = stack.pop() 
              
            if temp:
                temp.right = TreeNode(preorder[i]) 
                stack.append(temp.right) 
            else: 
                temp = stack[-1] 
                temp.left = TreeNode(preorder[i]) 
                stack.append(temp.left) 
            
            i += 1

        return root