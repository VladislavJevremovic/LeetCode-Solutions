// https://leetcode.com/problems/palindrome-number/

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 {
            return false
        }

        if x > 9 && x.isMultiple(of: 10) {
            return false
        }

        let original = x
        var flipped = 0
        var x = x
        while x > 0 {
            flipped = 10 * flipped + x % 10
            x /= 10
        }

        return original == flipped
    }
}
