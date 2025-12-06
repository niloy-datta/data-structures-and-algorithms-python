class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_any_pos(head, idx, val):
    newnode = Node(val)
    tmp = head
    for i in range(2, idx - 1):
        tmp = tmp.next
        if tmp is None:
            return
    newnode.next = tmp.next
    tmp.next = newnode

def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next

def main():
    head = Node(10)
    a = Node(20)
    b = Node(30)

    head.next = a
    a.next = b

    insert_at_any_pos(head, 3, 100)
    print_linked_list(head)

if __name__ == "__main__":
    main()
