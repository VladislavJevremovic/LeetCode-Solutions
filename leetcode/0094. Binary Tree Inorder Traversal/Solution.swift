// https://leetcode.com/problems/binary-tree-inorder-traversal/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }

        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    }
}
