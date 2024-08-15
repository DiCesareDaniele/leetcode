'''
https://leetcode.com/problems/k-closest-points-to-origin
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(-(p[0] * p[0] + p[1] * p[1]), p) for p in points[:k]]
        heapq.heapify(heap)
        for p in points[k:]:
            d = p[0] * p[0] + p[1] * p[1]
            if d < -heap[0][0]:
                heapq.heapreplace(heap, (-d, p))
        return [v[1] for v in heap]
