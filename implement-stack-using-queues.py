# https://leetcode.com/problems/implement-stack-using-queues/submissions/982628887/
from collections import deque


class MyStack:
    def __init__(self):
        self._elems = deque([], maxlen=100)

    def push(self, x: int) -> None:
        self._elems.append(x)

    def pop(self) -> int:
        for _ in range(len(self._elems) - 1):
            self.push(self._elems.popleft())
        return self._elems.popleft()

    def top(self) -> int:
        for _ in range(len(self._elems) - 1):
            self.push(self._elems.popleft())
        result = self._elems[0]
        self.push(self._elems.popleft())
        return result

    def empty(self) -> bool:
        return len(self._elems) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)
print(obj.pop())
print(obj.empty())
