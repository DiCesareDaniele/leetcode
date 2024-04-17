'''
https://leetcode.com/problems/generate-parentheses
'''

class Solution:
    # pylint: disable-next=invalid-name
    def generateParenthesis(self, n: int) -> list[str]:
        out = []
        def generate_helper(acc: str, opened: int, n: int):
            if len(acc) == 2 * n:
                out.append(acc)
                return
            if opened < n:
                generate_helper(acc + "(", opened + 1, n)
            if len(acc) < 2 * opened:
                generate_helper(acc + ")", opened, n)
        generate_helper("", 0, n)
        return out
