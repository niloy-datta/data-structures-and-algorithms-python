class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_tail(head_ref, val):
    newnode = Node(val)
    if head_ref[0] is None:
        head_ref[0] = newnode
        return

    tmp = head_ref[0]
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = newnode

def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next

def main():
    head = None
    # a = Node(20)
    # b = Node(30)

    # head.next = a
    # a.next = b

    head_ref = [head]
    insert_at_tail(head_ref, 40)
    insert_at_tail(head_ref, 50)
    insert_at_tail(head_ref, 60)
    print_linked_list(head_ref[0])

if __name__ == "__main__":
    main()
