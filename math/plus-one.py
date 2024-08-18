'''
https://leetcode.com/problems/plus-one
'''

class Solution:
    # pylint: disable-next=invalid-name
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        c = 1
        while i >= 0 and c > 0:
            d = digits[i] + c
            digits[i] = d % 10
            c = d // 10
            i -= 1
        if c > 0:
            digits.insert(0, 1)
        return digits
