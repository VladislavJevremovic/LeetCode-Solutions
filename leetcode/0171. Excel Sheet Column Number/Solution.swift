// https://leetcode.com/problems/excel-sheet-column-number/

class Solution {
    func titleToNumber(_ s: String) -> Int {
        let characters = Array(s).map { Character(String($0)) }
        let a_ord = Character("A").asciiValue ?? 0
        var multiplier = 1
        var result = 0
        for character in characters.reversed() {
            let character_ord = character.asciiValue ?? 0
            let difference = Int(character_ord - a_ord)
            result += (difference + 1) * multiplier
            multiplier *= 26
        }

        return result
    }
}

let s = Solution()
assert(s.titleToNumber("A") == 1)
assert(s.titleToNumber("B") == 2)
assert(s.titleToNumber("C") == 3)
assert(s.titleToNumber("Z") == 26)
assert(s.titleToNumber("AA") == 27)
assert(s.titleToNumber("AB") == 28)
assert(s.titleToNumber("ZY") == 701)
assert(s.titleToNumber("ZZ") == 702)
