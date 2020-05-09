# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r = r * 2 + int(n % 2)
            n /= 2
            
        return r

s = Solution()
assert s.reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
assert s.reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111
