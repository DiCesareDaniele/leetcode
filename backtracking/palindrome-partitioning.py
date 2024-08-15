'''
https://leetcode.com/problems/palindrome-partitioning
'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        sol = []
        sub = []
        def partition_helper(i: int):
            if i == len(s):
                sol.append(sub[:])
                return
            for j in range(i, len(s)):
                pal = s[i:j+1]
                if pal == pal[::-1]:
                    sub.append(pal)
                    partition_helper(j + 1)
                    sub.pop()
        partition_helper(0)
        return sol
