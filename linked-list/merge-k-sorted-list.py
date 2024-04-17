'''
https://leetcode.com/problems/merge-k-sorted-lists/description
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        def merge2(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            l = ListNode()
            h = l
            while l1 and l2:
                if l1.val < l2.val:
                    l.next = ListNode(val=l1.val)
                    l1 = l1.next
                else:
                    l.next = ListNode(val=l2.val)
                    l2 = l2.next
                l = l.next
            while l1:
                l.next = ListNode(val=l1.val)
                l = l.next
                l1 = l1.next
            while l2:
                l.next = ListNode(val=l2.val)
                l = l.next
                l2 = l2.next
            return h.next

        if not lists:
            return None

        while len(lists) > 1:
            answer = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                answer.append(merge2(l1, l2))
            lists = answer

        return lists[0]
