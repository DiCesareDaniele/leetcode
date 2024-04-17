'''
https://leetcode.com/problems/koko-eating-bananas
'''

class Solution:
    # pylint: disable-next=invalid-name
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat_all(k: int) -> bool:
            return sum((p // k) + (p % k > 0) for p in piles) <= h
        i = max(sum(piles) // h, 1)
        j = max(piles)
        while i < j:
            m = (i + j) // 2
            if can_eat_all(m):
                j = m
            else:
                i = m + 1
        return i
