# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        preorder_list = []
        self.preorder(root, preorder_list)
        
        return " ".join(str(item) for item in preorder_list)
        

    def deserialize(self, data: str) -> TreeNode:
        data = data.split()
        data.reverse() # use right pop
        
        return self.dfs(data)
        
    
    def preorder(self, root: TreeNode, preorder_list: List[int]) -> None:
        if not root:
            preorder_list.append(None)
            return
        
        preorder_list.append(root.val)
        self.preorder(root.left, preorder_list)
        self.preorder(root.right, preorder_list)

    
    def dfs(self, data: List[str]) -> TreeNode:
        if not data:
            return
        
        val = data.pop() # faster to pop off right
        if val == 'None':
            return None
        else:
            root = TreeNode(int(val))
        
        root.left = self.dfs(data)
        root.right = self.dfs(data)
        
        return root

codec = Codec()
codec.deserialize(codec.serialize(TreeNode(0)))
