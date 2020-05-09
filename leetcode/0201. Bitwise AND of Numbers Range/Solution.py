# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while m != n:
            m >>= 1 # chop off right side until equal
            n >>= 1
            c += 1

        return m << c # now pad right with c zeros

s = Solution()
assert s.rangeBitwiseAnd(5, 7) == 4
assert s.rangeBitwiseAnd(0, 1) == 0