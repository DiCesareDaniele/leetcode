'''
https://leetcode.com/problems/copy-list-with-random-pointer
'''

class Node:
    # pylint: disable-next=redefined-builtin
    def __init__(self, x: int, next: 'Node' | None = None, random: 'Node' | None = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # pylint: disable-next=invalid-name
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None
        nodes = {}
        h = head
        while h:
            nodes[h] = Node(h.val)
            h = h.next

        h = head
        while h:
            if h.next:
                nodes[h].next = nodes[h.next]
            if h.random:
                nodes[h].random = nodes[h.random]
            h = h.next

        return nodes[head]
