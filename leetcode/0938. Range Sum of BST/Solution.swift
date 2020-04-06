// https://leetcode.com/problems/range-sum-of-bst/

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
    func rangeSumBST(_ root: TreeNode?, _ L: Int, _ R: Int) -> Int {
        guard let root = root else { return 0 }

        var sum = 0
        sum += rangeSumBST(root.left, L, R)
        if L <= root.val && root.val <= R {
            sum += root.val
        }
        sum += rangeSumBST(root.right, L, R)

        return sum
    }
}
