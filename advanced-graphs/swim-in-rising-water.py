'''
https://leetcode.com/problems/swim-in-rising-water
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = [[False] * n for _ in range(n)]
        distances = [[1e10] * n for _ in range(n)]
        distances[0][0] = grid[0][0]
        heap = [(grid[0][0], (0, 0))]
        while len(heap) > 0:
            dist, (x0, y0) = heapq.heappop(heap)
            if x0 == n - 1 and y0 == n - 1:
                return dist
            if visited[x0][y0]:
                continue
            visited[x0][y0] = True

            for dx, dy in directions:
                x = x0 + dx
                y = y0 + dy
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue
                if visited[x][y]:
                    continue
                dist_j = max(dist, grid[x][y])
                if dist_j < distances[x][y]:
                    distances[x][y] = dist_j
                    heapq.heappush(heap, (dist_j, (x, y)))
        return -1
