// https://leetcode.com/problems/sqrtx/

class Solution {
    func mySqrt(_ x: Int) -> Int {
        if x < 2 { return x }

        var a = 2
        var b = x / 2

        while a < b {
            let m = a + (b - a) / 2
            if m * m > x {
                b = m - 1
            } else if m * m < x {
                if (m + 1) * (m + 1) > x {
                    return m
                }
                a = m + 1
            } else {
                return m
            }
        }

        return b
    }
}

let s = Solution()
assert(s.mySqrt(0) == 0)
assert(s.mySqrt(1) == 1)
assert(s.mySqrt(2) == 1)
assert(s.mySqrt(3) == 1)
assert(s.mySqrt(4) == 2)
assert(s.mySqrt(5) == 2)
assert(s.mySqrt(6) == 2)
assert(s.mySqrt(7) == 2)
assert(s.mySqrt(8) == 2)
assert(s.mySqrt(9) == 3)
