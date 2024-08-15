'''
https://leetcode.com/problems/subsets
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        sol = []
        sub = []
        def subsets_helper(i: int):
            if i == len(nums):
                sol.append(sub[:])
                return
            sub.append(nums[i])
            subsets_helper(i + 1)
            sub.pop()
            subsets_helper(i + 1)
        subsets_helper(0)
        return sol
