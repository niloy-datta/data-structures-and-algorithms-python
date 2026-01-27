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

def insert(root_ref, val):
    if root_ref[0] is None:
        root_ref[0] = Node(val)
    if root_ref[0].val > val:
        if root_ref[0].left is None:
            root_ref[0].left = Node(val)
        else:
            left_ref = [root_ref[0].left]
            insert(left_ref, val)
            root_ref[0].left = left_ref[0]
    else:
        if root_ref[0].right is None:
            root_ref[0].right = Node(val)
        else:
            right_ref = [root_ref[0].right]
            insert(right_ref, val)
            root_ref[0].right = right_ref[0]

def main():
    root = input_tree()
    val = int(cin())
    root_ref = [root]
    insert(root_ref, val)
    insert(root_ref, 11)
    level_order(root_ref[0])

if __name__ == "__main__":
    main()
