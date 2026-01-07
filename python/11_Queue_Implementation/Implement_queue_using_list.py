import sys
from collections import deque

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class myQueue:
    def __init__(self):
        self.l = deque()

    def push(self, val):      # O(1)
        self.l.append(val)

    def pop(self):         # O(1)
        self.l.popleft()

    def front(self):         # O(1)
        return self.l[0]

    def back(self):          # O(1)
        return self.l[-1]

    def size(self):         # O(1)
        return len(self.l)

    def empty(self):       # O(1)
        return len(self.l) == 0

def main():
    q = myQueue()
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        val = int(cin())
        q.push(val)

    while not q.empty():
        print(q.front())
        q.pop()

if __name__ == "__main__":
    main()
