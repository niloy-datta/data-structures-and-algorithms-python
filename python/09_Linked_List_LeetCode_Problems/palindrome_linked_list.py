# Problem link: https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert_at_tail(self, head_ref, tail_ref, val):
        newnode = ListNode(val)
        if head_ref[0] is None:
            head_ref[0] = newnode
            tail_ref[0] = newnode
            return
        tail_ref[0].next = newnode
        tail_ref[0] = newnode

    def reverse(self, head_ref, tmp):
        if tmp.next is None:
            head_ref[0] = tmp
            return
        self.reverse(head_ref, tmp.next)
        tmp.next.next = tmp
        tmp.next = None

    def isPalindrome(self, head: ListNode) -> bool:
        head_ref = [None]
        tail_ref = [None]

        tmp = head
        while tmp is not None:
            self.insert_at_tail(head_ref, tail_ref, tmp.val)
            tmp = tmp.next

        newhead_ref = [head_ref[0]]
        self.reverse(newhead_ref, newhead_ref[0])
        newhead = newhead_ref[0]

        tmp = head
        tmp2 = newhead

        while tmp is not None:
            if tmp.val != tmp2.val:
                return False
            tmp = tmp.next
            tmp2 = tmp2.next
        return True

# Using vector

class SolutionVector:
    def isPalindrome(self, head: ListNode) -> bool:
        v = []
        tmp = head
        while tmp is not None:
            v.append(tmp.val)
            tmp = tmp.next
        v2 = list(v)
        v2.reverse()
        return v == v2
