'''
https://leetcode.com/problems/kth-largest-element-in-a-stream
'''

import heapq

class KthLargest:
    heap: list[int]
    k: int

    def __init__(self, k: int, nums: list[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
