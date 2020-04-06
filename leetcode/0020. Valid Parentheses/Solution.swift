// https://leetcode.com/problems/valid-parentheses/

class Solution {
    func isValid(_ s: String) -> Bool {
        let map: [Character: Character] = [")": "(", "}": "{", "]": "["]
        var stack = [Character]()
        for c in s {
            if let d = map[c] {
                let topElement = stack.isEmpty ? "#" : stack.popLast()
                if topElement != d {
                    return false
                }
            } else {
                stack.append(c)
            }
        }

        return stack.isEmpty
    }
}

let s = Solution()
assert(s.isValid("()") == true)
assert(s.isValid("()[]{}") == true)
assert(s.isValid("(]") == false)
assert(s.isValid("([)]") == false)
assert(s.isValid("{[]}") == true)
