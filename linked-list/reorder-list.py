'''
https://leetcode.com/problems/reorder-list
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def reorderList(self, head: ListNode | None) -> None:
        if not head:
            return

        stack = []
        h = head
        while h:
            stack.append(h)
            h = h.next

        h = head
        while h.next and h.next.next:
            t = stack.pop()
            if stack:
                stack[-1].next = None
            t.next = h.next
            h.next = t
            h = t.next
        