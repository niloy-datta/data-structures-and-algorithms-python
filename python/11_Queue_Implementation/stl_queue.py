import sys
from collections import deque

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    q = deque()
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        val = int(cin())
        q.append(val)

    while len(q) > 0:
        print(q.popleft())

if __name__ == "__main__":
    main()
