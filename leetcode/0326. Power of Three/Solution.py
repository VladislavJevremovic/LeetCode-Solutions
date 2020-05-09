# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # The biggest power of 3 that fits into 32 bits is 3486784401 (3^20).
        # For signed 32 bits it is 1162261467 (3^19):
        # 3^floor(log_3 MAX) == pow(3, floor(log(MAX) / log(3)))
    	
        return n > 0 and not 1162261467 % n

    def isPowerOfThree(self, n: int) -> bool:	
        if n == 0:
        	return False
        if n == 1:
        	return True
        
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False

s = Solution()
assert s.isPowerOfThree(27) == True
assert s.isPowerOfThree(0) == False
assert s.isPowerOfThree(9) == True
assert s.isPowerOfThree(45) == False
assert s.isPowerOfThree(-3) == False
