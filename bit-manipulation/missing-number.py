'''
https://leetcode.com/problems/missing-number
'''

class Solution:
    # pylint: disable-next=invalid-name
    def missingNumber(self, nums: list[int]) -> int:
        bit_set = 0
        for i, n in enumerate(nums):
            bit_set = bit_set ^ n ^ i
        return bit_set ^ len(nums)
