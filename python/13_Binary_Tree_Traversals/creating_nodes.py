class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

    return 0

if __name__ == "__main__":
    main()
