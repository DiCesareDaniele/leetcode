'''
https://leetcode.com/problems/sliding-window-maximum
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        w_len = len(nums) - k + 1
        w = [0] * w_len
        q = []
        for i in range(k):
            heapq.heappush(q, (-nums[i], i))
        w[0] = -q[0][0]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            max_v = q[0]
            while i - max_v[1] >= k:
                heapq.heappop(q)
                max_v = q[0]
            w[i - k + 1] = -max_v[0]
        return w
        