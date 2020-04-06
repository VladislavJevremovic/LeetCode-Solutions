// https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var counts = [String: Int]()
        for c in s {
            let cs = String(c)
            counts[cs] = (counts[cs] ?? 0) + 1
        }
        
        for (i, c) in s.enumerated() {
            let cs = String(c)
            if (counts[cs] ?? 0) == 1 {
                return i
            }
        }
        
        
        return -1
    }
}