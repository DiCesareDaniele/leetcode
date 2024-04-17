'''
https://leetcode.com/problems/3sum
'''

class Solution:
    # pylint: disable-next=invalid-name
    def threeSum(self, numbers: list[int]) -> list[list[int]]:
        numbers.sort()
        possibilities = []
        previ = numbers[0] - 1
        for i in range(len(numbers) - 2):
            if numbers[i] == previ:
                continue
            previ = numbers[i]
            target = -numbers[i]
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                t = numbers[j] + numbers[k]
                if t > target:
                    k -= 1
                elif t < target:
                    j += 1
                else:
                    possibilities.append([numbers[i], numbers[j], numbers[k]])
                    prevj = numbers[j]
                    while j < len(numbers) and numbers[j] == prevj:
                        j += 1
                    prevk = numbers[k]
                    while k > 0 and numbers[k] == prevk:
                        k -= 1
        return possibilities
