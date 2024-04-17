'''
https://leetcode.com/problems/longest-consecutive-sequence
'''

class Solution:
    # pylint: disable-next=invalid-name
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_l = 0
        for n in num_set:
            if n - 1 in num_set:
                continue
            sequence_length = 1
            while n + sequence_length in num_set:
                sequence_length += 1
            max_l = max(max_l, sequence_length)
        return max_l
