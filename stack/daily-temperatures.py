'''
https://leetcode.com/problems/min-stack
'''

class Solution:
    # pylint: disable-next=invalid-name
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, ti in enumerate(temperatures):
            while stack and ti > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer
