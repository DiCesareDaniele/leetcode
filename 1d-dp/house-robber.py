'''
https://leetcode.com/problems/house-robber
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        DP[i] = max(DP[i - 1], nums[i] + DP[i - 2])
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        i = nums[0]
        j = max(i, nums[1])
        for k in range(2, len(nums)):
            tmp = j
            j = max(j, i + nums[k])
            i = tmp
        return max(i, j)
