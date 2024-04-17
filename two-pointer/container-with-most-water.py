'''
https://leetcode.com/problems/container-with-most-water
'''

class Solution:
    # pylint: disable-next=invalid-name
    def maxArea(self, height: list[int]) -> int:
        max_a = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j]) * (j - i)
            max_a = max(max_a, h)
            hi = height[i]
            hj = height[j]
            if hi >= hj:
                j -= 1
            if hj >= hi:
                i += 1
        return max_a
