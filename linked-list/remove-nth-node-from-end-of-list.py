'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        def remove_nth_helper(head: ListNode | None, n: int) -> int:
            if not head:
                return 0
            idx = remove_nth_helper(head.next, n)
            if idx == -1:
                return -1
            if idx == n:
                if head.next:
                    head.next = head.next.next
                else:
                    head.next = None
                return -1
            return idx + 1
        idx = remove_nth_helper(head, n)
        if idx != -1:
            return head.next
        return head
