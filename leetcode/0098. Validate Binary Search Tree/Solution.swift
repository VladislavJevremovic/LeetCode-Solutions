// https://leetcode.com/problems/validate-binary-search-tree/

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
    func isValidBST(_ root: TreeNode?, _ lowerBound: Int, _ upperBound: Int) -> Bool {
        guard let root = root else {
            return true
        }

        if root.val <= lowerBound || root.val >= upperBound {
            return false
        }

        return isValidBST(root.left, lowerBound, root.val) && isValidBST(root.right, root.val, upperBound)
    }

    func isValidBST(_ root: TreeNode?) -> Bool {
        return isValidBST(root, Int.min, Int.max)
    }
}