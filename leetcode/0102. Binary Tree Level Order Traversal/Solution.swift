// https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        var levels = [[Int]]()
        guard let root = root else {
            return levels
        }

        var q = [TreeNode]()
        q.append(root)

        var level = [Int]()
        while !q.isEmpty {
            for _ in 0..<q.count {
                let n = q.removeFirst()
                level.append(n.val)

                if let left = n.left {
                    q.append(left)
                }
                if let right = n.right {
                    q.append(right)
                }
            }

            levels.append(level)
            level = []
        }

        return levels
    }
}
