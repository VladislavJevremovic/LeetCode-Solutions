# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        q = collections.deque([root])
        
        level = []
        while q:
            c = len(q)
            for _ in range(c):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            levels.append(level)
            level = []
        
        return levels