// https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution {
    func trailingZeroes(_ n: Int) -> Int {
        if n == 0 { return 0 }
        return n / 5 + trailingZeroes(n / 5)
    }
}
