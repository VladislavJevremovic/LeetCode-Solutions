# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        r = []
        if not root:
            return r

        q = collections.deque()
        q.append(root)

        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node.val)
                q.extend(node.children)

            r.append(l)

        return r