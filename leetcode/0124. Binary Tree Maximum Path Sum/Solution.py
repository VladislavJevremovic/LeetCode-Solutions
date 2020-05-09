# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def sum(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_sum = sum(node.left)
            right_sum = sum(node.right)

            # current node may be temp root or on result path
            
            temp_max = node.val + max(0, left_sum, right_sum, left_sum + right_sum)
            self.result = max(self.result, temp_max)
            
            return node.val + max(0, left_sum, right_sum)
        
        self.result = -math.inf
        sum(root)
        
        return self.result