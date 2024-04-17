'''
https://leetcode.com/problems/reverse-nodes-in-k-group
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # pylint: disable-next=invalid-name
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse_k_group_helper(head: ListNode | None, k: int) -> \
            tuple[ListNode | None, ListNode | None, int]:
            prev = head
            curr = head.next
            head.next = None
            while curr and k > 1:
                next_n = curr.next
                curr.next = prev

                prev = curr
                curr = next_n
                k -= 1
            return (prev, curr, k - 1)

        h1 = head
        t1, h2, _ = reverse_k_group_helper(h1, k)
        tr = t1
        while h2:
            t2, h3, rem = reverse_k_group_helper(h2, k)
            if rem > 0:
                t2, h3, _ = reverse_k_group_helper(t2, k)
            h1.next = t2
            h1 = h2
            t1 = t2
            h2 = h3
        return tr
