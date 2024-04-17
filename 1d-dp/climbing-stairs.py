'''
https://leetcode.com/problems/climbing-stairs
'''

class Solution:
    # pylint: disable-next=invalid-name
    def climbStairs(self, n: int) -> int:
        def fib(n: int) -> int:
            i = 0
            j = 1
            for _ in range(n):
                tmp = j
                j += i
                i = tmp
            return i
        return fib(n + 1)
