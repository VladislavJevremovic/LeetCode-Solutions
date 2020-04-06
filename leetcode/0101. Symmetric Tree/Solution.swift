// https://leetcode.com/problems/symmetric-tree/

class Solution {
    func isSymmetric(_ root: TreeNode?) -> Bool {
        return isMirrored(root, root)
    }
    
    func isMirrored(_ t1: TreeNode?, _ t2: TreeNode?) -> Bool {
        if t1 == nil && t2 == nil { return true }
        if t1 == nil || t2 == nil { return false }
        
        return t1!.val == t2!.val
            && isMirrored(t1?.right, t2?.left)
            && isMirrored(t1?.left, t2?.right)
        }
}