'''
https://leetcode.com/problems/set-matrix-zeroes
'''

class Solution:
    # pylint: disable-next=invalid-name
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in zero_row:
            for j in range(n):
                matrix[i][j] = 0

        for j in zero_col:
            for i in range(m):
                matrix[i][j] = 0
