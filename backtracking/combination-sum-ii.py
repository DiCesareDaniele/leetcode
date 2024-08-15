'''
https://leetcode.com/problems/combination-sum-ii
'''

class Solution:
    # pylint: disable-next=invalid-name
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        sol = []
        sub = []
        nums.sort()
        def combination_sum_helper(i: int, partial_sum: int):
            if partial_sum == target:
                sol.append(sub[:])
                return
            if partial_sum > target or i >= len(nums):
                return
            sub.append(nums[i])
            combination_sum_helper(i + 1, partial_sum + nums[i])
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            sub.pop()
            combination_sum_helper(i + 1, partial_sum)
        combination_sum_helper(0, 0)
        return sol
