# Problem link: https://leetcode.com/problems/min-stack/description/

class MinStack:
    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min_st) == 0:
            self.min_st.append(val)
        elif self.min_st[-1] >= val:
            self.min_st.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.min_st[-1]:
            self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
