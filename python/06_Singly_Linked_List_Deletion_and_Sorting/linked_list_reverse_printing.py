import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_tail(head_ref, tail_ref, val):
    newnode = Node(val)
    if head_ref[0] is None:
        head_ref[0] = newnode
        tail_ref[0] = newnode
        return
    tail_ref[0].next = newnode
    tail_ref[0] = newnode

def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next

def print_reverse(tmp):
    if tmp is None:
        return
    print_reverse(tmp.next)
    print(tmp.val)

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

    print_reverse(head_ref[0])

if __name__ == "__main__":
    main()
