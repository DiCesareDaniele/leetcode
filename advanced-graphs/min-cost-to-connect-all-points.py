'''
https://leetcode.com/problems/min-cost-to-connect-all-points
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        visited = [False] * n
        costs = [1e10] * n
        tree_cost = 0

        while len(heap) > 0:
            cost, i = heapq.heappop(heap)
            if visited[i]:
                continue
            visited[i] = True
            tree_cost += cost

            for j in range(n):
                if visited[j]:
                    continue
                adj_cost = (
                    abs(points[i][0] - points[j][0]) +
                    abs(points[i][1] - points[j][1])
                )
                if adj_cost < costs[j]:
                    costs[j] = adj_cost
                    heapq.heappush(heap, (adj_cost, j))
        return tree_cost
