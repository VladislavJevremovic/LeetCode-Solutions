// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

public class TreeNode {
    public var val: Int
    public var children: [TreeNode?]
    public init(_ val: Int) {
        self.val = val
        self.children = []
    }
}

class Solution {
    func preorder(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }

        var r = [root.val]
        for child in root.children {
            r += preorder(child)
        }

        return r
    }
}
