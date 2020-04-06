// https://leetcode.com/problems/reverse-bits/

class Solution {
    func reverseBits(_ n: UInt32) -> UInt32 {
        var r = UInt32(0), n = n
        for _ in 0..<32 {
            r = r * 2 + n % 2
            n /= 2
        }

        return r
    }
}

let s = Solution()
assert(s.reverseBits(UInt32("00000010100101000001111010011100", radix: 2)!) == UInt32("00111001011110000010100101000000", radix: 2)!)
assert(s.reverseBits(UInt32("11111111111111111111111111111101", radix: 2)!) == UInt32("10111111111111111111111111111111", radix: 2)!)
