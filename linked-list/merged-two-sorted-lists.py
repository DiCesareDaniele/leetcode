'''
https://leetcode.com/problems/merge-two-sorted-lists
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        l1 = list1
        l2 = list2
        m = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    m.next = l1
                    l1 = l1.next
                else:
                    m.next = l2
                    l2 = l2.next
            elif l1:
                m.next = l1
                l1 = l1.next
            else:
                m.next = l2
                l2 = l2.next
            m = m.next
        return dummy.next
