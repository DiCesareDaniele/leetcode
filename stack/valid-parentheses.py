'''
https://leetcode.com/problems/valid-parentheses
'''

class Solution:
    # pylint: disable-next=invalid-name
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {"(": ")", "[": "]", "{": "}"}
        for p in s:
            if p in parentheses_map:
                stack.append(p)
            else:
                if not stack:
                    return False
                opened = stack.pop()
                closed = parentheses_map[opened]
                if closed != p:
                    return False
        return len(stack) == 0
