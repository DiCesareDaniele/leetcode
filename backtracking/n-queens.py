'''
https://leetcode.com/problems/n-queens
'''

class Solution:
    # pylint: disable-next=invalid-name
    def solveNQueens(self, n: int) -> list[list[str]]:
        sol = []
        queens = list(range(n))
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]
        def queen_helper(row: int):
            if row == n:
                sol.append(["".join(r) for r in board])
                return
            for row_swap in range(row, n):
                col = queens[row_swap]
                if row + col in pos_diag or row - col in neg_diag:
                    continue
                board[row][col] = "Q"
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                queens[row], queens[row_swap] = queens[row_swap], queens[row]
                queen_helper(row + 1)
                queens[row], queens[row_swap] = queens[row_swap], queens[row]
                board[row][col] = "."
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
        queen_helper(0)
        return sol
