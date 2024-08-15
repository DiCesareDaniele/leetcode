'''
https://leetcode.com/problems/last-stone-weight
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))
        if len(heap) == 0:
            return 0
        return -heap[0]
