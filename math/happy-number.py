'''
https://leetcode.com/problems/happy-number
'''

class Solution:
    # pylint: disable-next=invalid-name
    def isHappy(self, n: int) -> bool:
        def sum_squared_digits(n: int) -> int:
            sum_sq = 0
            while n > 0:
                d = n % 10
                sum_sq += d * d
                n //= 10
            return sum_sq
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = sum_squared_digits(n)
        return False
