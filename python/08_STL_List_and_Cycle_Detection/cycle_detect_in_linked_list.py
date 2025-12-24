class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main():
    head = Node(10)
    a = Node(20)
    b = Node(30)
    c = Node(40)
    d = Node(50)

    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = d

    slow = head
    fast = head
    flag = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            flag = True
            break
    if flag == True:
        print("Cycle Detected")
    else:
        print("No Cycle")

if __name__ == "__main__":
    main()
