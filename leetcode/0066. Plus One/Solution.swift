// https://leetcode.com/problems/plus-one/

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var result = [Int]()
        var carry = 1
        for digit in digits.reversed() {
            let sum = digit + carry
            result.append(sum % 10)
            carry = sum / 10
        }
        if carry > 0 {
            result.append(carry)
        }
        
        return result.reversed()
    }
}