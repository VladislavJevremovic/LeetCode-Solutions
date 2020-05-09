# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        
s = Solution()

l = ["h","e","l","l","o"]
s.reverseString(l)
assert l == ["o","l","l","e","h"]

l = ["H","a","n","n","a","h"]
s.reverseString(l)
assert l == ["h","a","n","n","a","H"]
