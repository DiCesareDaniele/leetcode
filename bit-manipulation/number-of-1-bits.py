'''
https://leetcode.com/problems/number-of-1-bits
'''

class Solution:
    # pylint: disable-next=invalid-name
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n > 0:
            set_bits += n & 1
            n = n >> 2
        return set_bits
