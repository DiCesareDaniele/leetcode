'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    # pylint: disable-next=invalid-name
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            t = numbers[i] + numbers[j]
            if t > target:
                j -= 1
            elif t < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return [0, 0]
