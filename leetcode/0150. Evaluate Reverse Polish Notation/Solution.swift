// https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution {
    func evalRPN(_ tokens: [String]) -> Int {
        var stack = [String]()

        let pop: (inout [String]) -> Int = { stack in
            return Int(stack.removeLast()) ?? 0
        }

        for token in tokens {
            switch token {
            case "+":
                let (b, a) = (pop(&stack), pop(&stack))
                stack.append("\(a + b)")
                break
            case "-":
                let (b, a) = (pop(&stack), pop(&stack))
                stack.append("\(a - b)")
                break
            case "*":
                let (b, a) = (pop(&stack), pop(&stack))
                stack.append("\(a * b)")
                break
            case "/":
                let (b, a) = (pop(&stack), pop(&stack))
                stack.append("\(a / b)")
                break
            default:
                stack.append(token)
                break
            }
        }

        return Int(stack.removeLast()) ?? 0
    }
}

let s = Solution()
assert(s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
assert(s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
assert(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22)
