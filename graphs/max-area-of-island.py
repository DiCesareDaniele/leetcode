'''
https://leetcode.com/problems/max-area-of-island
'''

class Solution:
    # pylint: disable-next=invalid-name
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return (
                1
                + dfs(i + 1, j)
                + dfs(i - 1, j)
                + dfs(i, j + 1)
                + dfs(i, j - 1)
            )
        area = 0
        for i in range(m):
            for j in range(n):
                area = max(area, dfs(i, j))
        return area
