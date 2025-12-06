class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_head(head, val):
    newnode = Node(val)
    newnode.next = head
    head = newnode
    return head

def print_linked_list(head):
    tmp = head
    while tmp.next is not None:
        print(tmp.val)
        tmp = tmp.next

def main():
    head = Node(10)
    a = Node(20)
    b = Node(30)

    head.next = a
    a.next = b

    print_linked_list(head)

if __name__ == "__main__":
    main()
