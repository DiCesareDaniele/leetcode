'''
https://leetcode.com/problems/maximum-product-subarray
'''

class Solution:
    # pylint: disable-next=invalid-name
    def maxProduct(self, nums: list[int]) -> int:
        prod = 1
        max_so_far = nums[0]
        # exclude last negative
        for n in nums:
            prod *= n
            max_so_far = max(max_so_far, prod)
            if n == 0:
                prod = 1
        prod = 1
        # exclude first negative
        for n in reversed(nums):
            prod *= n
            max_so_far = max(max_so_far, prod)
            if n == 0:
                prod = 1
        return max_so_far
