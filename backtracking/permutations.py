'''
https://leetcode.com/problems/permutations
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        sol = []
        def permute_helper(i: int):
            if i == len(nums):
                sol.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permute_helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        permute_helper(0)
        return sol
