// https://leetcode.com/problems/valid-palindrome/

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        if s.isEmpty { return true }

        let sArray = Array(s).map { String($0).lowercased() }

        var a = 0, b = sArray.count - 1
        while a < b {
            while a < sArray.count && !sArray[a].isAlphanumeric {
                a += 1
            }
            while b >= 0 && !sArray[b].isAlphanumeric {
                b -= 1
            }

            if a >= sArray.count || b < 0 { return true }

            if sArray[a] != sArray[b] {
                return false
            }

            a += 1
            b -= 1
        }

        return true
    }
}

extension String {
    var isAlphanumeric: Bool {
        return !isEmpty && range(of: "[^a-zA-Z0-9]", options: .regularExpression) == nil
    }
}