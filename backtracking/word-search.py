'''
https://leetcode.com/problems/word-search
'''

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        def exist_helper(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i >= m or j >= n or i < 0 or j < 0:
                return False
            if visited[i][j] or word[k] != board[i][j]:
                return False
            visited[i][j] = True
            if (
                exist_helper(i + 1, j, k + 1) or
                exist_helper(i - 1, j, k + 1) or
                exist_helper(i, j + 1, k + 1) or
                exist_helper(i, j - 1, k + 1)
            ):
                return True
            visited[i][j] = False
            return False
        for i in range(m):
            for j in range(n):
                if exist_helper(i, j, 0):
                    return True
        return False
