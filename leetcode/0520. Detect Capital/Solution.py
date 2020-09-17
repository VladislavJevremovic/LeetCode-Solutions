# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        p = ""
        for i, c in enumerate(word):
            if i > 0 and p.islower() and c.isupper():
                return False
            if i > 1 and p.isupper() and c.islower():
                return False
            p = c

        return True


s = Solution()
assert s.detectCapitalUse("USA") == True
assert s.detectCapitalUse("leetcode") == True
assert s.detectCapitalUse("Google") == True
assert s.detectCapitalUse("FlaG") == False
assert s.detectCapitalUse("") == True
assert s.detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf") == False
assert s.detectCapitalUse("Leetcode") == True
