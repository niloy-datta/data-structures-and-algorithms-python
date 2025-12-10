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
    tail_ref[0] = tail_ref[0].next

def insert_at_head(head_ref, tail_ref, val):
    newnode = Node(val)
    if head_ref[0] is None:
        head_ref[0] = newnode
        tail_ref[0] = newnode
        return
    newnode.next = head_ref[0]
    head_ref[0] = newnode

def insert_at_any_pos(head_ref, idx, val):
    newnode = Node(val)
    tmp = head_ref[0]
    for i in range(1, idx):
        tmp = tmp.next
        if tmp is None:
            return
    newnode.next = tmp.next
    tmp.next = newnode

def size_linked_list(head):
    cnt = 0
    tmp = head
    while tmp is not None:
        cnt += 1
        tmp = tmp.next
    return cnt

def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

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

    while True: # for queries
        tok_idx = cin()
        if tok_idx is None:
            break
        idx = int(tok_idx)
        val = int(cin())
        sz = size_linked_list(head_ref[0])
        if idx > sz:
            print("Invalid")
            continue
        elif idx == sz:
            insert_at_tail(head_ref, tail_ref, val)
        elif idx == 0:
            insert_at_head(head_ref, tail_ref, val)
        else:
            insert_at_any_pos(head_ref, idx, val)
        print_linked_list(head_ref[0])

if __name__ == "__main__":
    main()
