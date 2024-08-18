'''
https://leetcode.com/problems/powx-n
'''

class Solution:
    # pylint: disable-next=invalid-name
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        p = x
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= p
            p *= p
            n >>= 1
        return res
