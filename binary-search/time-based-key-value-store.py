'''
https://leetcode.com/problems/time-based-key-value-store
'''

from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(times: list[tuple[int, str]], timestamp: int) -> str:
            i = 0
            j = len(times)
            while i < j:
                m = (i + j) // 2
                if times[m][0] > timestamp:
                    j = m
                else:
                    i = m + 1
            return "" if i == 0 else times[i - 1][1]
        if key not in self.time_map:
            return ""
        times = self.time_map[key]
        return binary_search(times, timestamp)
