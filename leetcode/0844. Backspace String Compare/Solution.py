# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def make_string(s):
            r = []
            for c in s:
                if c != '#':
                    r.append(c)
                elif r:
                    r.pop()
            
            return "".join(r)

        return make_string(S) == make_string(T)