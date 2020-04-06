// https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }

        return inorderTraversal(root.left) + inorderTraversal(root.right) + [root.val]
    }
}
