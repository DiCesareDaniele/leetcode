'''
https://leetcode.com/problems/evaluate-reverse-polish-notation
'''

import math

class Solution:
    # pylint: disable-next=invalid-name
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = "+-*/"
        for token in tokens:
            if token in ops:
                t2 = stack.pop()
                t1 = stack.pop()
                if token == "+":
                    stack.append(t1 + t2)
                elif token == "-":
                    stack.append(t1 - t2)
                elif token == "*":
                    stack.append(t1 * t2)
                elif token == "/":
                    stack.append(math.trunc(t1 / t2))
            else:
                stack.append(int(token))
        return stack.pop()
