'''
https://leetcode.com/problems/merge-intervals
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        intervals.sort(key=lambda i: i[0])
        i = 0
        ans = []
        while i < n:
            start, end = intervals[i]
            while i < n and end >= intervals[i][0]:
                end = max(end, intervals[i][1])
                i += 1
            ans.append([start, end])
        return ans
