// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
    func convertToTitle(_ n: Int) -> String {
        var result = ""
        var n = n
        while n > 0 {
            var r = n % 26
            n /= 26
            if r == 0 {
                if n >= 1 {  r = 26 }
                n -= 1 // n = r + 26 * (1 + 26 * (1 + ...
            }

            let a_ord = Character("A").asciiValue ?? 0
            let c = Character(UnicodeScalar(Int(a_ord) + r - 1) ?? " ")
            result = String(c) + result
        }

        return result
    }
}

let s = Solution()
assert(s.convertToTitle(1) == "A")
assert(s.convertToTitle(2) == "B")
assert(s.convertToTitle(3) == "C")
assert(s.convertToTitle(26) == "Z")
assert(s.convertToTitle(27) == "AA")
assert(s.convertToTitle(28) == "AB")
assert(s.convertToTitle(701) == "ZY")
assert(s.convertToTitle(702) == "ZZ")
