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

def main():
    head = Node(10)
    a = Node(20)
    tail = Node(30)

    head.next = a
    a.next = tail

    head_ref = [head]
    tail_ref = [tail]

    insert_at_tail(head_ref, tail_ref, 40)
    insert_at_tail(head_ref, tail_ref, 50)
    insert_at_tail(head_ref, tail_ref, 60)
    print_linked_list(head_ref[0])
    print("Tail =", tail_ref[0].val)

if __name__ == "__main__":
    main()
