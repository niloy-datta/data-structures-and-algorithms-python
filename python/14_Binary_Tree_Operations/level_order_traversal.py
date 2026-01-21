from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        # 1. ber kore ana
        f = q.popleft()

        # 2. oi node ke niye kaj
        print(f.val, end=" ")

        # 3. children push kora
        if f.left:
            q.append(f.left)
        if f.right:
            q.append(f.right)

def main():
    root = Node(10)
    a = Node(20)
    b = Node(30)
    c = Node(40)
    d = Node(50)
    e = Node(60)

    root.left = a
    root.right = b
    a.left = c
    b.left = d
    b.right = e

    level_order(root)

if __name__ == "__main__":
    main()
