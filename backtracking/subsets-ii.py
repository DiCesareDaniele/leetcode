'''
https://leetcode.com/problems/subsets-ii
'''

class Solution:
    # pylint: disable-next=invalid-name
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        sol = []
        sub = []
        nums.sort()
        def subsets_helper(i: int):
            if i == len(nums):
                sol.append(sub[:])
                return
            sub.append(nums[i])
            subsets_helper(i + 1)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            sub.pop()
            subsets_helper(i + 1)
        subsets_helper(0)
        return sol
