'''
https://leetcode.com/problems/task-scheduler
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        m = max(freq)
        mc = freq.count(m)
        return max(len(tasks), (n + 1) * (m - 1) + mc)
