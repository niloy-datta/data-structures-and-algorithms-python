import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def print_forward(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

def insert_at_tail(head_ref, tail_ref, val):
    newnode = Node(val)
    if head_ref[0] is None:
        head_ref[0] = newnode
        tail_ref[0] = newnode
        return
    tail_ref[0].next = newnode
    newnode.prev = tail_ref[0]
    tail_ref[0] = newnode

def main():
    head_ref = [None]
    tail_ref = [None]

    while True:
        tok = cin()
        if tok is None:
            break
        val = int(tok)
        if val == -1:
            break
        insert_at_tail(head_ref, tail_ref, val)

    print_forward(head_ref[0])

if __name__ == "__main__":
    main()
