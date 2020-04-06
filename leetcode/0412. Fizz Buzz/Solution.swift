// https://leetcode.com/problems/fizz-buzz/

class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var r = [String]()
        
        for i in 1...n {
            if i % 15 == 0 {
                r.append("FizzBuzz")
            } else if i % 3 == 0 {
                r.append("Fizz")
            } else if i % 5 == 0 {
                r.append("Buzz")
            } else {
                r.append("\(i)")
            }
        }

        return r
    }
}