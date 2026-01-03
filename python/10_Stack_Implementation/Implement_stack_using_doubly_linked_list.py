import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class myStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def push(self, val):       # O(1)
        self.sz += 1
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def pop(self):           # O(1)
        self.sz -= 1
        deletenode = self.tail
        self.tail = self.tail.prev
        del deletenode
        if self.tail is None:
            self.head = None
            return
        self.tail.next = None

    def top(self):        # O(1)
        return self.tail.val

    def size(self):       # O(1)
        return self.sz

    def empty(self):      # O(1)
        return self.head is None

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
