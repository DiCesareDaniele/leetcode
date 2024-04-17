'''
https://leetcode.com/problems/lru-cache
'''

class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, n: ListNode):
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def remove(self, n: ListNode):
        if n.prev is None: 
            self.remove_head()
        elif n.next is None:
            self.remove_tail()
        else:
            n.next.prev = n.prev
            n.prev.next = n.next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        m = ListNode(key=key, val=n.val)
        self.lru.remove(n)
        self.lru.add(m)
        self.cache[key] = m
        return n.val

    def put(self, key: int, value: int) -> None:
        n = ListNode(key=key, val=value)
        if key not in self.cache:
            if self.capacity == 0:
                h = self.lru.head
                del self.cache[h.key]
                self.lru.remove_head()
            else:
                self.capacity -= 1
            self.lru.add(n)
        else:
            m = self.cache[key]
            self.lru.remove(m)
            self.lru.add(n)
        self.cache[key] = n
