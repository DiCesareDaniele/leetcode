'''
https://leetcode.com/problems/search-a-2d-matrix
'''

class Solution:
    # pylint: disable-next=invalid-name
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ms = len(matrix)
        ns = len(matrix[0])
        i = 0
        j = ms * ns
        while i < j:
            m = (i + j) // 2
            if matrix[m // ns][m % ns] > target:
                j = m
            elif matrix[m // ns][m % ns] < target:
                i = m + 1
            else:
                return True
        return False
