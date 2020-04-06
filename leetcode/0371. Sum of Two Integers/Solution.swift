// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    func getSum(_ a: Int, _ b: Int) -> Int {
        if b == 0 {
            return a
        } else {
            return getSum(a ^ b, (a & b) << 1)
        }
    }
}