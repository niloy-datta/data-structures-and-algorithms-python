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

def print_backward(tail):
    tmp = tail
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.prev
    print()

def main():
    head = Node(10)
    a = Node(20)
    tail = Node(30)

    head.next = a
    a.prev = head

    a.next = tail
    tail.prev = a

    print_forward(head)
    print_backward(tail)

if __name__ == "__main__":
    main()
