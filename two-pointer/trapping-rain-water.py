'''
https://leetcode.com/problems/trapping-rain-water
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = 1
        area = 0
        while j < len(height):
            if height[i] > height[j]:
                j += 1
                continue
            hi = height[i]
            while i < j:
                area += hi - height[i]
                i += 1
            j += 1

        i = len(height) - 1
        j = len(height) - 2
        while j >= 0:
            if height[i] >= height[j]:
                j -= 1
                continue
            hi = height[i]
            while i > j:
                area += hi - height[i]
                i -= 1
            j -= 1
        return area
