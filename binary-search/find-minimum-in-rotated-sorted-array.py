'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
'''

class Solution:
    # pylint: disable-next=invalid-name
    def findMin(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)
        while i < j:
            m = (i + j) // 2
            if nums[0] > nums[m]:
                j = m
            else:
                i = m + 1
        return nums[i % len(nums)]
