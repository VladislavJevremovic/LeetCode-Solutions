// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    func tribonacci(_ n: Int) -> Int {
        if n == 0 { return 0 }
        if case 1...2 = n { return 1 }

        var f = Array(repeating: 0, count: n + 1)
        f[0] = 0
        f[1] = 1
        f[2] = 1

        for i in 3...n {
            f[i] = f[i - 1] + f[i - 2] + f[i - 3]
        }
        
        return f[n]
    }
}

let s = Solution()
assert(s.tribonacci(0) == 0)
assert(s.tribonacci(1) == 1)
assert(s.tribonacci(2) == 1)
assert(s.tribonacci(3) == 2)
assert(s.tribonacci(4) == 4)
assert(s.tribonacci(25) == 1389537)
