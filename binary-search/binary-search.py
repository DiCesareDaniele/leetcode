'''
https://leetcode.com/problems/binary-search
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            m = (i + j) // 2
            if nums[m] > target:
                j = m
            elif nums[m] < target:
                i = m + 1
            else:
                return m
        return -1
