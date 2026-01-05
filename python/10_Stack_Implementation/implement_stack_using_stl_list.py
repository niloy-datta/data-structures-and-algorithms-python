import sys
from collections import deque

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class myStack:
    def __init__(self):
        self.l = deque()

    def push(self, val):
        self.l.append(val)

    def pop(self):
        self.l.pop()

    def top(self):
        return self.l[-1]

    def size(self):
        return len(self.l)

    def empty(self):
        return len(self.l) == 0

def main():
    st = myStack()
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        x = int(cin())
        st.push(x)

    while not st.empty():
        print(st.top())
        st.pop()

if __name__ == "__main__":
    main()
