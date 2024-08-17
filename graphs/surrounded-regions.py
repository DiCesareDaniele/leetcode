'''
https://leetcode.com/problems/surrounded-regions
'''

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        edges = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if edges[x][y] or board[x][y] == "X":
                return
            edges[x][y] = True
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        for x in range(m):
            dfs(x, 0)
            dfs(x, n - 1)
        for y in range(n):
            dfs(0, y)
            dfs(m - 1, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O" and not edges[x][y]:
                    board[x][y] = "X"
