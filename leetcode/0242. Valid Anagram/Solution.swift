// https://leetcode.com/problems/valid-anagram/

class Solution { // slow
    func isAnagram(_ s: String, _ t: String) -> Bool {
        return s.sorted() == t.sorted()
    }
}

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var d = [Int](repeating: 0, count: 26)
        let a = Character("a").asciiValue ?? 0
        for c in s {
            let cv = Character(String(c)).asciiValue ?? 0
            d[Int(cv - a)] += 1
        }
        for c in t {
            let cv = Character(String(c)).asciiValue ?? 0
            d[Int(cv - a)] -= 1
        }

        for c in d {
            if c != 0 {
                return false
            }
        }

        return true
    }
}