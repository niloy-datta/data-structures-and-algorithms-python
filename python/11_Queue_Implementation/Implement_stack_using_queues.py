from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        q2 = deque()
        while len(self.q) > 0:
            val = self.q.popleft()
            if len(self.q) == 0:
                break
            q2.append(val)
        self.q = q2
        return val

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
