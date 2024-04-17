'''
https://leetcode.com/problems/min-stack
'''

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min_v, _ = self.stack[-1]
            min_v = min(min_v, val)
        else:
            min_v = val
        self.stack.append((min_v, val))

    def pop(self) -> None:
        _, v = self.stack.pop()
        return v

    def top(self) -> int:
        return self.stack[-1][1]

    # pylint: disable-next=invalid-name
    def getMin(self) -> int:
        return self.stack[-1][0]
