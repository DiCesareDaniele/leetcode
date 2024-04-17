'''
https://leetcode.com/problems/two-sum
'''

class Solution:
    # pylint: disable-next=invalid-name
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_set = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in nums_set:
                return [nums_set[c], i]
            nums_set[n] = i
        return [-1, -1]
