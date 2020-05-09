# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        if n < 2:
            return True

        a = 2
        b = n // 2
        while a <= b:
            m = a + (b - a) // 2
            if m * m > n:
                b = m - 1
            elif m * m < n:
                a = m + 1
            else:
                return True

        return False

s = Solution()
assert s.isPerfectSquare(0) == True
assert s.isPerfectSquare(8) == False
assert s.isPerfectSquare(9) == True
assert s.isPerfectSquare(16) == True
