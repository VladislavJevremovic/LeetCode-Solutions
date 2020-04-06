// https://leetcode.com/problems/count-and-say/

class Solution {
    func countAndSay(_ n: Int) -> String {
        var s = "1"
        for _ in 1..<n {
            s = say(s)
        }

        return s
    }

    func say(_ s: String) -> String {
        let sa = Array(s).map { String($0) }
        var r = ""

        var i = 0
        while i < sa.count {
            var count = 1
            while i + 1 < sa.count && sa[i] == sa[i + 1] {
                i += 1
                count += 1
            }
            r += "\(count)" + sa[i]
            i += 1
        }

        return r
    }
}

let s = Solution()
assert(s.countAndSay(1) == "1")
assert(s.countAndSay(2) == "11")
assert(s.countAndSay(3) == "21")
assert(s.countAndSay(4) == "1211")
assert(s.countAndSay(5) == "111221")
assert(s.countAndSay(6) == "312211")
assert(s.countAndSay(7) == "13112221")
assert(s.countAndSay(8) == "1113213211")