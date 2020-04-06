// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

public class TreeNode {
    public var val: Int
    public var children: [TreeNode?]
    public init(_ val: Int) {
        self.val = val
        self.children = []
    }
}

class Solution {
    func postorder(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }

        var r = [Int]()
        for child in root.children {
            r += postorder(child)
        }

        return r + [root.val]
    }
}
