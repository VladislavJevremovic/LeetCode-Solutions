# https://leetcode.com/problems/ransom-note/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if not ransomNote:
        #     return True

        # if not magazine:
        #     return False
        
        # r_c = Counter(ransomNote)
        # r_m = Counter(magazine)
        # for w in r_c:
        #     if r_m[w] < r_c[w]:
        #         return False
        
        # return True

        return not len(Counter(ransomNote) - Counter(magazine)) # deletes only matching pairs

s = Solution()
assert s.canConstruct("", "b") == True
assert s.canConstruct("a", "") == False
assert s.canConstruct("a", "b") == False
assert s.canConstruct("aa", "ab") == False
assert s.canConstruct("aa", "aab") == True
assert s.canConstruct("aa", "aaab") == True