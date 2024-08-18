'''
https://leetcode.com/problems/non-overlapping-intervals
'''

class Solution:
    # pylint: disable-next=invalid-name
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        overlap = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                overlap += 1
            else:
                prev_end = end
        return overlap
