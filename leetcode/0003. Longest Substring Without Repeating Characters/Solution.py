// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hs = set()
        r, i, j = 0, 0, 0
        
        while i < n and j < n:
            if s[j] not in hs:
                hs.add(s[j])
                j += 1
                r = max(r, j - i)
            else:
                hs.discard(s[i])
                i += 1
        
        return r