// https://leetcode.com/problems/first-bad-version

class Solution {
    func firstBadVersion(_ n: Int) -> Int {
        var a = 1
        var b = n
        while a < b {
            let m = a + (b - a) / 2
            if isBadVersion(m) {
                b = m
            } else {
                a = m + 1
            }
        }

        return a
    }
}

extension Solution {
    func isBadVersion(_ n: Int) -> Bool {
        return n == 4
    }
}

let s = Solution()
assert(s.firstBadVersion(5) == 4)
