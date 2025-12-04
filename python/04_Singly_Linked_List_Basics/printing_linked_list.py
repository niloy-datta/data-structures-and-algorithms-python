class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main():
    head = Node(10)
    a = Node(20)
    b = Node(30)
    c = Node(400)

    head.next = a
    a.next = b
    b.next = c

    # print(head.val)
    # print(head.next.val)
    # print(head.next.next.val)
    # print(head.next.next.next.val)
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next

if __name__ == "__main__":
    main()
