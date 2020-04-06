// https://leetcode.com/problems/min-stack/

class MinStack {

    typealias Element = (value: Int, minimum: Int)

    private var stack = [Element]()

    func push(_ x: Int) {
        stack.append(Element(value: x, minimum: stack.isEmpty ? x : min(x, getMin())))
    }

    func pop() {
        _ = stack.removeLast()
    }

    func top() -> Int {
        return stack.last?.value ?? Int.min
    }

    func getMin() -> Int {
        return stack.last?.minimum ?? Int.min
    }
}

class MinStack<T: Numeric & Comparable> {

    typealias Element = (value: T, minimum: T)

    private var stack = [Element]()

    func push(_ x: T) {
        stack.append(Element(value: x, minimum: stack.isEmpty ? x : min(x, getMin())))
    }

    func pop() {
        _ = stack.removeLast()
    }

    func top() -> T {
        return stack.last?.value ?? T.zero
    }

    func getMin() -> T {
        return stack.last?.minimum ?? T.zero
    }
}

let s = MinStack<Int>()
s.push(-2)
s.push(0)
s.push(-3)
assert(s.getMin() == -3)
s.pop()
assert(s.top() == 0)
assert(s.getMin() == -2)
