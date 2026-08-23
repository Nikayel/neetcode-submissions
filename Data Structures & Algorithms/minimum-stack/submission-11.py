class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack and self.minStack[-1] >= val:
            self.minStack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack and self.stack[-1] == self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]