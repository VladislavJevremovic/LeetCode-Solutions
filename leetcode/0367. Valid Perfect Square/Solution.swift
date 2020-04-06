// https://leetcode.com/problems/valid-perfect-square/

class Solution {
    func isPerfectSquare(_ n: Int) -> Bool {
        if n < 2 { return true }

        var a = 2
        var b = n / 2

        while a <= b {
            let m = a + (b - a) / 2
            if m * m > n {
                b = m - 1
            } else if m * m < n {
                a = m + 1
            } else {
                return true
            }
        }

        return false
    }
}

let s = Solution()
assert(s.isPerfectSquare(0) == true)
assert(s.isPerfectSquare(8) == false)
assert(s.isPerfectSquare(9) == true)
assert(s.isPerfectSquare(16) == true)
