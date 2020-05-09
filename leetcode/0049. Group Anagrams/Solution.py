# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = collections.defaultdict(list)
        for s in strs:
            r[tuple(sorted(s))].append(s)
            
        return r.values()