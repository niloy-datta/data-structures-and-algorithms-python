class MyQueue:
    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        st2 = []
        while len(self.st) > 0:
            val = self.st.pop()
            if len(self.st) == 0:
                break
            st2.append(val)
        while len(st2) > 0:
            self.st.append(st2.pop())
        return val

    def peek(self) -> int:
        st2 = []
        while len(self.st) > 0:
            val = self.st.pop()
            st2.append(val)
        while len(st2) > 0:
            self.st.append(st2.pop())
        return val

    def empty(self) -> bool:
        return len(self.st) == 0
