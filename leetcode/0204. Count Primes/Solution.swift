// https://leetcode.com/problems/count-primes/

class Solution {
    func countPrimes(_ n: Int) -> Int {
        if n < 2 { return 0 }

        var isPrime = [Bool](repeating: true, count: n)
        isPrime[0] = false
        isPrime[1] = false

        var p = 2
        while p * p < n {
            if isPrime[p] {
                var i = p * p
                while i < n {
                    isPrime[i] = false
                    i += p
                }
            }
            p += 1
        }

        var count = 0
        for i in 2..<n {
            if isPrime[i] {
                count += 1
            }
        }

        return count
    }
}

let s = Solution()
assert(s.countPrimes(10) == 4)
assert(s.countPrimes(20) == 8)
