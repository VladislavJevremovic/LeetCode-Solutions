// https://leetcode.com/problems/subtree-of-another-tree/

class Solution {
    func isSubtree(_ s: TreeNode?, _ t: TreeNode?) -> Bool {
        if s == nil { return false }
        if t == nil { return true }
        return isSameTree(s, t) || isSubtree(s?.left, t) || isSubtree(s?.right, t)
    }
    
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        if p == nil && q == nil { return true }
        return (p?.val == q?.val) && isSameTree(p?.left, q?.left) && isSameTree(p?.right, q?.right)
    }
}