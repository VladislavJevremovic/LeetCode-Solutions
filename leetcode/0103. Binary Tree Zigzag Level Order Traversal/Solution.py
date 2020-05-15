# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            r = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    r.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            r = r[::-1] if len(result) % 2 else r
            if r:
                result.append(r)

        return result

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        Q = [root]
        right_start = 0
        if root:
            while Q:
                l = len(Q)
                levels.append([])
                for i in range(l):
                    cur = Q.pop(0)
                    if cur.left:
                        Q.append(cur.left)
                    if cur.right:
                        Q.append(cur.right)
                    levels[-1].append(cur.val)
                if right_start & 1:
                    levels[-1] = levels[-1][::-1]
                right_start ^= 1

        return levels