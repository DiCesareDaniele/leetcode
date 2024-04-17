'''
https://leetcode.com/problems/sum-of-two-integers
'''

class Solution:
    # pylint: disable-next=invalid-name
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        while b & mask > 0:
            c = (a & b) << 1
            # sum without carry
            a = a ^ b
            # add carry
            b = c
        # handle overflow
        return a & mask if b > 0 else a
