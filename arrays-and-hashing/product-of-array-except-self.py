'''
https://leetcode.com/problems/product-of-array-except-self
'''

class Solution:
    # pylint: disable-next=invalid-name
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        acc = [1] * n
        prefix = 1
        suffix = 1
        for i in range(n):
            acc[i] *= prefix
            acc[n - i - 1] *= suffix
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
        return acc
