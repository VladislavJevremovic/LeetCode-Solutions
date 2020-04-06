// https://leetcode.com/problems/maximum-depth-of-n-ary-tree

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        depth, nodes = 0, [root]
        while nodes:
            depth += 1
            nodes = [child for node in nodes for child in node.children]
        
        return depth


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root.children:
                return 1
            else:
                return max(dfs(i) for i in root.children) + 1
        
        if root:
            return dfs(root)
        else:
            return 0