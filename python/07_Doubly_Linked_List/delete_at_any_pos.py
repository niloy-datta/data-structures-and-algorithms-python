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

def delete_at_any_pos(head, idx):
    tmp = head
    for i in range(1, idx):
        tmp = tmp.next
    deleteNode = tmp.next
    tmp.next = tmp.next.next
    tmp.next.prev = tmp
    del deleteNode

def main():
    head = Node(10)
    a = Node(20)
    tail = Node(30)

    head.next = a
    a.prev = head

    a.next = tail
    tail.prev = a

    delete_at_any_pos(head, 1)
    print_forward(head)

if __name__ == "__main__":
    main()
