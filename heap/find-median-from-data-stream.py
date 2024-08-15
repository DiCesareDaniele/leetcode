'''
https://leetcode.com/problems/find-median-from-data-stream
'''

import heapq

class MedianFinder:
    lheap: list[int]
    rheap: list[int]

    def __init__(self):
        self.lheap = []
        self.rheap = []

    # pylint: disable-next=invalid-name
    def addNum(self, num: int) -> None:
        if len(self.lheap) == len(self.rheap):
            x = heapq.heappushpop(self.rheap, num)
            heapq.heappush(self.lheap, -x)
        else:
            x = -heapq.heappushpop(self.lheap, -num)
            heapq.heappush(self.rheap, x)

    # pylint: disable-next=invalid-name
    def findMedian(self) -> float:
        if len(self.lheap) == len(self.rheap):
            return (-self.lheap[0] + self.rheap[0]) / 2
        return -self.lheap[0]
