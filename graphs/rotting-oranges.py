'''
https://leetcode.com/problems/rotting-oranges
'''

from collections import deque

class Solution:
    # pylint: disable-next=invalid-name
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rotten = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        minute = 0
        count = len(rotten)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while count > 0:
            x, y = rotten.popleft()
            for dx, dy in directions:
                i = x + dx
                j = y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 2
                    rotten.append((i, j))
            count -= 1
            if count == 0:
                count = len(rotten)
                if count > 0:
                    minute += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minute
