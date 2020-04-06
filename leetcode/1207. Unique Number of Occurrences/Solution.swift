// https://leetcode.com/problems/unique-number-of-occurrences

class Solution {
    func uniqueOccurrences(_ arr: [Int]) -> Bool {
        var counts = [Int: Int]()
        for n in arr {
            if !counts.keys.contains(n) {
                counts[n] = 0
            } else {
                counts[n] = (counts[n] ?? 0) + 1
            }
        }

        return Set(Array(counts.values)).count == counts.count
    }
}

let s = Solution()
assert(s.uniqueOccurrences([1,2,2,1,1,3]) == true)
assert(s.uniqueOccurrences([1,2]) == false)
assert(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == true)
