'''
https://leetcode.com/problems/house-robber-ii
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        DP[i] = max(DP[i - 1], nums[i] + DP[i - 2])
        '''
        def rob_helper(nums: list[int]) -> int:
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
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
