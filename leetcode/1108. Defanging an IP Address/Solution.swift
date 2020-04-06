// https://leetcode.com/problems/defanging-an-ip-address/

class Solution {
    func defangIPaddr(_ address: String) -> String {
        var result = ""
        for c in address {
            result.append(c == "." ? "[.]" : String(c))
        }

        return result
    }
}

let s = Solution()
assert(s.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1")
assert(s.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0")
