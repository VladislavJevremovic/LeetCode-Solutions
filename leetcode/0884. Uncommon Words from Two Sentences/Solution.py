# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import List
from collections import defaultdict, Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split() + B.split())

        return [word for word in c if c[word] == 1]

s = Solution()
assert s.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
assert s.uncommonFromSentences("apple apple", "banana") == ["banana"]