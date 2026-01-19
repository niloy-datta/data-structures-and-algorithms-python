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

def input_tree():
    val_tok = cin()
    if val_tok is None:
        return None
    val = int(val_tok)
    if val == -1:
        root = None
    else:
        root = Node(val)
    q = deque()
    if root:
        q.append(root)
    while len(q) > 0:
        # 1. ber kore ana
        p = q.popleft()

        # 2. oi node ke niye kaj
        l = int(cin())
        r = int(cin())
        if l == -1:
            myLeft = None
        else:
            myLeft = Node(l)
        if r == -1:
            myRight = None
        else:
            myRight = Node(r)

        p.left = myLeft
        p.right = myRight

        # 3. children push kora
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)

    return root

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    l = count_leaf_nodes(root.left)
    r = count_leaf_nodes(root.right)
    return l + r

def main():
    root = input_tree()
    print(count_leaf_nodes(root))

if __name__ == "__main__":
    main()
