import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class myStack:
    def __init__(self):
        self.v = []

    def push(self, val):
        self.v.append(val)

    def pop(self):
        self.v.pop()

    def top(self):
        return self.v[-1]

    def size(self):
        return len(self.v)

    def empty(self):
        return len(self.v) == 0

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
