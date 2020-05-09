# https://leetcode.com/problems/valid-palindrome/

class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     l, r = 0, len(s) - 1
        
    #     while l <= r:
    #         if s[l].isalnum() and s[r].isalnum():
    #             if s[l].lower() == s[r].lower():
    #                 l += 1
    #                 r -= 1
    #             else:
    #                 return False
    #         elif s[l].isalnum():
    #             r -= 1
    #         else:
    #             l += 1
                
    #     return True
    
    def isPalindrome(self, s: str) -> bool:
        if not len(s):
            return True

        s_array = list(s.lower())
        n = len(s_array)

        a, b = 0, n - 1
        while a < b:
            # proceed from left ignoring non-alphanumeric characters
            while a < n and not s_array[a].isalnum():
                a += 1

            # proceed from right ignoring non-alphanumeric characters
            while b >= 0 and not s_array[b].isalnum():
                b -= 1

            if a >= n or b < 0:
                return True

            if s_array[a] != s_array[b]:
                return False

            a += 1
            b -= 1

        return True

s = Solution()
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
