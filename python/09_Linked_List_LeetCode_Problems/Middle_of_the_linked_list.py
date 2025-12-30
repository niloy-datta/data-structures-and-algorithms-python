# Problem link: https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def size(self, head: ListNode) -> int:
        tmp = head
        cnt = 0
        while tmp is not None:
            cnt += 1
            tmp = tmp.next
        return cnt

    def middleNode(self, head: ListNode) -> ListNode:
        sz = self.size(head)
        tmp = head
        for i in range(1, sz // 2 + 1):
            tmp = tmp.next
        return tmp
