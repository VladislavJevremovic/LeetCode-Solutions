// https://leetcode.com/problems/reverse-integer/

class Solution {
    func reverse(_ x: Int) -> Int {
        var result = 0
        let sign = x < 0 ? -1 : 1
        var x = abs(x)
        while x > 0 {
            result = 10 * result + x % 10
            x /= 10
        }

        let r = sign * result
        return (r < Int32.min || r > Int32.max) ? 0 : r
    }
}

let s = Solution()
assert(s.reverse(0) == 0)
assert(s.reverse(123) == 321)
assert(s.reverse(-123) == -321)
assert(s.reverse(120) == 21)
assert(s.reverse(1534236469) == 0)
