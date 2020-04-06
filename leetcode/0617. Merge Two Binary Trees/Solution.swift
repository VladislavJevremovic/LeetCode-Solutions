// https://leetcode.com/problems/merge-two-binary-trees/

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
    func mergeTrees(_ t1: TreeNode?, _ t2: TreeNode?) -> TreeNode? {
        if t1 == nil && t2 == nil {
            return nil
        } else if t1 == nil {
            return t2
        } else if t2 == nil {
            return t1
        } else {
            let tmp = TreeNode(t1!.val + t2!.val)
            tmp.left = self.mergeTrees(t1!.left, t2!.left)
            tmp.right = self.mergeTrees(t1!.right, t2!.right)

            return tmp
        }
    }
}
