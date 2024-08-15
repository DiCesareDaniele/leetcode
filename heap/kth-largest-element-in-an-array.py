'''
https://leetcode.com/problems/kth-largest-element-in-an-array
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]
