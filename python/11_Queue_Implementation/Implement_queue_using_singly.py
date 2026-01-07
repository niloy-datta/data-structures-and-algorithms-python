import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class myQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def push(self, val):      # O(1)
        self.sz += 1
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        self.tail.next = newnode
        self.tail = newnode

    def pop(self):         # O(1)
        self.sz -= 1
        deleteNode = self.head
        self.head = self.head.next
        del deleteNode
        if self.head is None:
            self.tail = None

    def front(self):         # O(1)
        return self.head.val

    def back(self):          # O(1)
        return self.tail.val

    def size(self):
        return self.sz

    def empty(self):
        return self.head is None

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
