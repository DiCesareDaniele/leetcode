'''
https://leetcode.com/problems/pacific-atlantic-water-flow
'''

class Solution:
    # pylint: disable-next=invalid-name
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])
        visited_a = [[False] * n for _ in range(m)]
        visited_p = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x: int, y: int, visited: list[list[bool]], prev_height: int):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if visited[x][y] or heights[x][y] < prev_height:
                return
            visited[x][y] = True
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited, heights[x][y])

        for x in range(m):
            dfs(x, 0, visited_p, heights[x][0])
            dfs(x, n - 1, visited_a, heights[x][n - 1])
        for y in range(n):
            dfs(0, y, visited_p, heights[0][y])
            dfs(m - 1, y, visited_a, heights[m - 1][y])

        return [
            [x, y]
                for x in range(m)
                    for y in range(n)
            if visited_a[x][y] and visited_p[x][y]
        ]
