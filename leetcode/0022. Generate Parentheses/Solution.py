# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        
        def bt(s = '', l = 0, r = 0):
            if len(s) == 2 * n:
                a.append(s)
                return
            
            if l < n:
                bt(s + '(', l + 1, r)
            
            if r < l:
                bt(s + ')', l, r + 1)
            
        bt()
        
        return a