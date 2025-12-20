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

def delete_at_head(head_ref, tail_ref):
    deleteNode = head_ref[0]
    head_ref[0] = head_ref[0].next
    del deleteNode
    if head_ref[0] is None:
        tail_ref[0] = None
        return
    head_ref[0].prev = None

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

    delete_at_head(head_ref, tail_ref)
    delete_at_head(head_ref, tail_ref)
    print_forward(head_ref[0])

if __name__ == "__main__":
    main()
