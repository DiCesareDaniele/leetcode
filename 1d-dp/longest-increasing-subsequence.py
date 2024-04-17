'''
https://leetcode.com/problems/longest-increasing-subsequence
'''

class Solution:
    # pylint: disable-next=invalid-name
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        max_s = 0
        s = [0] * len(nums)
        for n, i in range(len(nums)):
            s[i] = 1
            for j in range(i):
                if n > nums[j] and s[i] < s[j] + 1:
                    s[i] = s[j] + 1
                if s[i] > max_s:
                    max_s = s[i]
        return max_s
