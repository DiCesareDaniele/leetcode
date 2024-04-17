'''
https://leetcode.com/problems/reverse-integer
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        rev = 0
        while x != 0:
            rev *= 10
            rev += x % 10
            if rev >= (1 << 31):
                return 0
            x //= 10
        return rev
