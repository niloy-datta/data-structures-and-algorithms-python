# Problem link: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head_ref, tmp):
        if tmp.next is None:
            head_ref[0] = tmp
            return
        self.reverse(head_ref, tmp.next)
        tmp.next.next = tmp
        tmp.next = None

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        head_ref = [head]
        self.reverse(head_ref, head)
        return head_ref[0]
