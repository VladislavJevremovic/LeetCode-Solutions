// https://leetcode.com/problems/roman-to-integer/

class Solution {
    func romanToInt(_ s: String) -> Int {
        let values: [Character: Int] = ["I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000]
        let reverseCharacters = Array(s).reversed()

        var result = 0
        var previousDigit = 0
        for c in reverseCharacters {
            let v = values[c] ?? 0
            result += (v < previousDigit) ? -v : v
            previousDigit = v
        }

        return result
    }
}

let s = Solution()
assert(s.romanToInt("III") == 3)
assert(s.romanToInt("IV") == 4)
assert(s.romanToInt("IX") == 9)
assert(s.romanToInt("LVIII") == 58)
assert(s.romanToInt("MCMXCIV") == 1994)
