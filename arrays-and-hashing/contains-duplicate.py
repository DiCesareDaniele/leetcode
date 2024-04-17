'''
https://leetcode.com/problems/contains-duplicate
'''

class Solution:
    # pylint: disable-next=invalid-name
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
