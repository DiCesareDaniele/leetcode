'''
https://leetcode.com/problems/find-the-duplicate-number
'''

class Solution:
    # pylint: disable-next=invalid-name
    def findDuplicate(self, nums: list[int]) -> int:
        i = nums[0]
        j = nums[nums[0]]
        while i != j:
            i = nums[i]
            j = nums[nums[j]]

        i = 0
        while i != j:
            i = nums[i]
            j = nums[j]
        return i
