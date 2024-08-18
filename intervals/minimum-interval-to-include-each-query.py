'''
https://leetcode.com/problems/minimum-interval-to-include-each-query
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        n = len(intervals)
        intervals.sort(key=lambda i: i[0])

        heap = []
        ans = {}

        i = 0
        for q in sorted(queries):
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, [r - l + 1, r])
                i += 1
            while len(heap) > 0 and q > heap[0][1]:
                heapq.heappop(heap)
            ans[q] = heap[0][0] if len(heap) > 0 else -1
        return [ans[q] for q in queries]
