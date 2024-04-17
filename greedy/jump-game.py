'''
https://leetcode.com/problems/jump-game
'''

class Solution:
    # pylint: disable-next=invalid-name
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        reach = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= reach:
                reach = i
        return reach == 0
