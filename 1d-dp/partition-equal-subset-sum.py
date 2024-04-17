'''
https://leetcode.com/problems/partition-equal-subset-sum
'''

class Solution:
    # pylint: disable-next=invalid-name
    def canPartition(self, nums: list[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        dp = [False] * (tot + 1)
        dp[tot // 2] = True
        for n in nums:
            for curr in range(tot, tot // 2 - 1, -1):
                no_take = dp[curr]
                take = dp[curr - n] if curr >= n else False
                dp[curr] = take or no_take
        return dp[tot]
