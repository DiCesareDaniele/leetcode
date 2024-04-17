'''
https://leetcode.com/problems/reverse-linked-list
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        stack = []
        t = head
        while t:
            stack.append(t)
            t = t.next

        l = stack.pop()
        t = l
        while stack:
            t.next = stack.pop()
            t = t.next
        t.next = None
        return l
