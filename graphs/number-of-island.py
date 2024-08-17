'''
https://leetcode.com/problems/number-of-islands
'''

class Solution:
    # pylint: disable-next=invalid-name
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if visited[i][j] or grid[i][j] == "0":
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                dfs(i, j)
                count += 1
        return count
