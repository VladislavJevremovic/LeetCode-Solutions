// https://leetcode.com/problems/unique-binary-search-trees/

class Solution {
    func numTrees(_ n: Int) -> Int {
        if n <= 1 {
            return 1
        }
        
        var f = [Int](repeating: 0, count: n + 1)
        f[0] = 1
        f[1] = 1
        for r in 2...n {
            for k in 1...r {
                f[r] += f[k - 1] * f[r - k]
            }
        }        
        
        return f[n]
    }
}