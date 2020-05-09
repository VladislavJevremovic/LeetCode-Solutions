# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in pairs:
                top = '?' if not stack else stack.pop()
                if top != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack

s = Solution()
assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("([)]") == False
assert s.isValid("{[]}") == True
