class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        # top = self.stack[-1]
        # self.stack.remove(top)
        if self.stack: self.stack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]
        else: return None

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()