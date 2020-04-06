// https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        if root == nil {
            return 0
        }

        return max(maxDepth(root?.left), maxDepth(root?.right)) + 1
    }
}