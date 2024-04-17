'''
https://leetcode.com/problems/top-k-frequent-elements
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        return [f for f, _ in freq.most_common(k)]
