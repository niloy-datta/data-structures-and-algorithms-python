import sys
from collections import deque

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        f = q.popleft()

        print(f.val, end=" ")

        if f.left:
            q.append(f.left)
        if f.right:
            q.append(f.right)

def convert(a, n, l, r):
    if l > r:
        return None
    mid = (l + r) // 2
    root = Node(a[mid])
    leftroot = convert(a, n, l, mid - 1)
    rightroot = convert(a, n, mid + 1, r)
    root.left = leftroot
    root.right = rightroot
    return root

def main():
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    a = [0] * n
    for i in range(n):
        a[i] = int(cin())
    root = convert(a, n, 0, n - 1)
    level_order(root)

if __name__ == "__main__":
    main()
