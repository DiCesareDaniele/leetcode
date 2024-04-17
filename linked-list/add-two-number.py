'''
https://leetcode.com/problems/add-two-numbers
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1i = l1
        l2i = l2
        rem = 0
        dummy = ListNode()
        h = dummy
        while l1i or l2i:
            if l1i and l2i:
                v = l1i.val + l2i.val + rem
                l1i = l1i.next
                l2i = l2i.next
            elif l1i:
                v = l1i.val + rem
                l1i = l1i.next
            else:
                v = l2i.val + rem
                l2i = l2i.next
            rem = v // 10
            v = v % 10
            h.next = ListNode(val=v)
            h = h.next
        if rem:
            h.next = ListNode(val=rem)
        return dummy.next
