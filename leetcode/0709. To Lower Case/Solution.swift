// https://leetcode.com/problems/to-lower-case/

class Solution {
    func toLowerCase(_ s: String) -> String {
        var result = ""
        for c in s {
            let v = c.asciiValue ?? 0
            if 65...90 ~= v {
                result.append(Character(UnicodeScalar(v + 32)))
            } else {
                result.append(c)
            }
        }

        return result
    }
}

let s = Solution()
assert(s.toLowerCase("Hello") == "hello")
assert(s.toLowerCase("here") == "here")
assert(s.toLowerCase("LOVELY") == "lovely")
