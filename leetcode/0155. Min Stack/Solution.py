# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        min_value = 0
        if not self.stack:
            min_value = x
        else:
            min_value = min(x, self.getMin())
        self.stack.append((x, min_value))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            (v, m) = self.stack[-1]
            return v
        else:
            return 0
        

    def getMin(self) -> int:
        if self.stack:
            (v, m) = self.stack[-1]
            return m
        else:
            return 0

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.getMin() == -3
min_stack.pop()
assert min_stack.top() == 0
assert min_stack.getMin() == -2
