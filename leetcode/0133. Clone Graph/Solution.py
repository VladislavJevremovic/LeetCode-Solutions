# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        self.visited[node] = Node(node.val, [])
        
        if node.neighbors:
            for n in node.neighbors:
                self.visited[node].neighbors.append(self.cloneGraph(n))
        
        return self.visited[node]