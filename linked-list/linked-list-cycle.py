'''
https://leetcode.com/problems/linked-list-cycle
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # pylint: disable-next=invalid-name
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        rabbit = head
        turtle = head
        while rabbit:
            rabbit = rabbit.next
            if rabbit is None:
                return False
            rabbit = rabbit.next
            turtle = turtle.next
            if rabbit == turtle:
                return True
        return False
