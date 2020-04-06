// https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution {
    func searchBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        guard let root = root else { return nil }
        
        if root.val == val {
            return root
        }
        
        let l = searchBST(root.left, val)
        if l != nil {
            return l
        }
        
        let r = searchBST(root.right, val)
        if r != nil {
            return r
        }
        
        return nil
    }
}
