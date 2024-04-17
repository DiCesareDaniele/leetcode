'''
https://leetcode.com/problems/maximum-subarray
'''

class Solution:
    # pylint: disable-next=invalid-name
    def maxSubArray(self, nums: list[int]) -> int:
        max_here = 0
        max_so_far = nums[0]
        for n in nums:
            max_here = max(n, max_here + n)
            max_so_far = max(max_so_far, max_here)
        return max_so_far
