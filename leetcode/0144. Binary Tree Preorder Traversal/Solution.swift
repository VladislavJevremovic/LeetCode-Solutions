// https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }

        return [root.val] + inorderTraversal(root.left) + inorderTraversal(root.right)
    }
}