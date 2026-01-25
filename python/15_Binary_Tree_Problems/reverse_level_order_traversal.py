# Problem link: https://www.codingninjas.com/studio/problems/reverse-level-order-traversal_764339
from collections import deque

def reverseLevelOrder(root):
    v = []
    q = deque()
    if root:
        q.append(root)
    while len(q) > 0:
        f = q.popleft()

        v.append(f.val)

        if f.left:
            q.append(f.left)
        if f.right:
            q.append(f.right)

    v.reverse()
    return v
