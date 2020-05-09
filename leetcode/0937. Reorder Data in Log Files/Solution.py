# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            ident, rest = log.split(" ", 1)
            return (0, rest, ident) if rest[0].isalpha() else (1,)
            
        return sorted(logs, key=f)