# https://leetcode.com/problems/implement-queue-using-stacks/submissions/985641293/
# very little memory but slow
# https://leetcode.com/problems/implement-queue-using-stacks/submissions/985651492/
# much faster but more memory
from collections import deque


class MyQueue:
    def __init__(self):
        self._elems = deque([], maxlen=100)
        self._dummy = deque([], maxlen=100)

    def push(self, x: int) -> None:
        for _ in range(len(self._elems)):
            self._dummy.append(self._elems.pop())
        self._elems.append(x)
        for _ in range(len(self._dummy)):
            self._elems.append(self._dummy.pop())

    def pop(self) -> int:
        return self._elems.pop()

    def peek(self) -> int:
        return self._elems[-1]

    def empty(self) -> bool:
        return len(self._elems) == 0


class MyQueue2:
    def __init__(self):
        self.in_stack = deque([], maxlen=100)
        self.out_stack = deque([], maxlen=100)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_1 = obj.peek()
print(param_1)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
print(obj.pop())
print(obj.empty())
