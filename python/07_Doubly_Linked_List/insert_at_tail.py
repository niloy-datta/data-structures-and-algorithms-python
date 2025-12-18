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
    head = Node(10)
    a = Node(20)
    tail = Node(30)

    head.next = a
    a.prev = head

    a.next = tail
    tail.prev = a

    head_ref = [head]
    tail_ref = [tail]

    insert_at_tail(head_ref, tail_ref, 100)
    insert_at_tail(head_ref, tail_ref, 200)
    print_forward(head_ref[0])

if __name__ == "__main__":
    main()
