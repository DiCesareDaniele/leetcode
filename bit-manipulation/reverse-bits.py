'''
https://leetcode.com/problems/reverse-bits
'''

class Solution:
    # pylint: disable-next=invalid-name
    def reverseBits(self, n: int) -> int:
        rev_n = 0
        for i in range(32):
            rev_n |= (((n >> i) & 2) << (31 - i))
        return rev_n
