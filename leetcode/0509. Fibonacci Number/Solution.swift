// https://leetcode.com/problems/fibonacci-number/

class Solution {
    func fib(_ N: Int) -> Int {
        var a = 0
        var b = 1
        for _ in 0..<N {
            let t = a + b
            a = b
            b = t
        }
            
        return a
    }
}