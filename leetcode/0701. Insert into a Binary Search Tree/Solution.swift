// https://leetcode.com/problems/insert-into-a-binary-search-tree

public class TreeNode {
    public var val: Int
    public var children: [TreeNode?]
    public init(_ val: Int) {
        self.val = val
        self.children = []
    }
}

class Solution {
    func insertIntoBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
		guard let root = root else {
			return TreeNode(val)
        }

		if val < root.val {
            root.left = insertIntoBST(root.left, val)
        } else {
            root.right = insertIntoBST(root.right, val)
        }

		return root
    }
}