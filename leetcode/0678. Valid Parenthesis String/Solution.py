# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_p, max_p, l = 0, 0, list(s)
        for c in l:
            if c == "(":
                min_p += 1
                max_p += 1
            elif c == ")":
                min_p -= 1
                max_p -= 1
            else:
                min_p -= 1
                max_p += 1
            
            if max_p < 0:
                return False
            min_p = max(min_p, 0)
        
        return min_p == 0

s = Solution()
assert s.checkValidString("()") == True
assert s.checkValidString("(*)") == True
assert s.checkValidString("(*))") == True
assert s.checkValidString("(*))(") == False
