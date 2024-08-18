'''
https://leetcode.com/problems/spiral-matrix
'''

class Solution:
    # pylint: disable-next=invalid-name
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        direction = 1
        ans = []
        i = 0
        j = -1
        while m > 0 and n > 0:
            for _ in range(n):
                j += direction
                ans.append(matrix[i][j])
            m -= 1
            for _ in range(m):
                i += direction
                ans.append(matrix[i][j])
            n -= 1
            direction *= -1
        return ans
