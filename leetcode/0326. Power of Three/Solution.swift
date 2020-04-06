// https://leetcode.com/problems/power-of-three/

class Solution {
    func isPowerOfThree(_ n: Int) -> Bool {
        if n == 0 { return false }
        if n == 1 { return true }
        
        if n.isMultiple(of: 3) {
            return isPowerOfThree(n / 3)
        } else {
            return false
        }
    }
}