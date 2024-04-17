'''
https://leetcode.com/problems/largest-rectangle-in-histogram
'''

class Solution:
    # pylint: disable-next=invalid-name
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_rect = 0
        for h in heights:
            w = 0
            while stack and stack[-1][1] >= h:
                wi, hi = stack.pop()
                w += wi
                max_rect = max(max_rect, w * hi)
            stack.append((w + 1, h))
        w = 0
        while stack:
            wi, hi = stack.pop()
            w += wi
            max_rect = max(max_rect, w * hi)
        return max_rect
