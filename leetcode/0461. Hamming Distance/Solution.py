# https://leetcode.com/problems/hamming-distance/

class Solution {
    func hammingDistance(_ x: Int, _ y: Int) -> Int {
        var z = x ^ y, c = 0
        
        while z > 0 {
            c += z & 1
            z >>= 1
        }

        return c
    }
}