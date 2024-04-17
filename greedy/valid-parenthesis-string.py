'''
https://leetcode.com/problems/valid-parenthesis-string
'''

class Solution:
    # pylint: disable-next=invalid-name
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        for p in s:
            if p == "(":
                max_open += 1
                min_open += 1
            elif p == ")":
                max_open -= 1
                min_open = max(min_open - 1, 0)
            else:
                max_open += 1
                min_open = max(min_open - 1, 0)
            if max_open < 0:
                return False
        return min_open == 0
