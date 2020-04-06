// https://leetcode.com/problems/jewels-and-stones/

class Solution {
    func numJewelsInStones(_ J: String, _ S: String) -> Int {
        var count = 0
        for c in S {
            if J.contains(c) {
                count += 1
            }
        }

        return count
    }
}

let s = Solution()
assert(s.numJewelsInStones("aA", "aAAbbbb") == 3)
assert(s.numJewelsInStones("z", "ZZ") == 0)