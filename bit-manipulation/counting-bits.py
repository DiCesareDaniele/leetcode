'''
https://leetcode.com/problems/counting-bits
'''

class Solution:
    # pylint: disable-next=invalid-name
    def countBits(self, n: int) -> list[int]:
        cb = [0] * (n + 1)
        for i in range(1, n + 1):
            cb[i] = cb[i >> 2] + (i & 1)
        return cb
