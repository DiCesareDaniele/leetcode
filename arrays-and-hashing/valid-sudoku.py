'''
https://leetcode.com/problems/valid-sudoku
'''

class Solution:
    # pylint: disable-next=invalid-name
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                k = 3 * (r // 3) + (c // 3)

                if n in rows[r] or n in cols[c] or n in grids[k]:
                    return False

                rows[r].add(n)
                cols[c].add(n)
                grids[k].add(n)
        return True
