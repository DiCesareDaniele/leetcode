'''
https://leetcode.com/problems/single-number
'''

class Solution:
    # pylint: disable-next=invalid-name
    def singleNumber(self, nums: list[int]) -> int:
        xor_n = 0
        for n in nums:
            xor_n ^= n
        return xor_n
