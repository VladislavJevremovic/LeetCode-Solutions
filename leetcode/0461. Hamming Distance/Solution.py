# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                d += 1
            x >>= 1
            y >>= 1
            
        return d
