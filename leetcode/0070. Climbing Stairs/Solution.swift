// https://leetcode.com/problems/climbing-stairs/

class Solution {
    func climbStairs(_ n: Int) -> Int {
        if n < 2 {
            return 1
        }
        
        var f = Array(repeating: 0, count: n + 1)
        f[0] = 1
        f[1] = 1
        for i in 2...n {
            f[i] = f[i - 1] + f[i - 2]
        }
        
        return f[n]
    }
}