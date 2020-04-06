// https://leetcode.com/problems/unique-morse-code-words/

class Solution {
    let m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    func tranformation(_ word: String) -> String {
        var r = ""
        for c in word {
            let diff = Int((c.asciiValue ?? 0) - (Character("a").asciiValue ?? 0))
            r += m[diff]
        }

        return r
    }

    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        var s = Set<String>()
        for word in words {
            s.insert(tranformation(word))
        }

        return s.count
    }
}

let s = Solution()
assert(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2)
