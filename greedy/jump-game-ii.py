'''
https://leetcode.com/problems/jump-game-ii
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        reach = 0
        end = 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == end:
                end = reach
                jumps += 1
        return jumps
