'''
https://leetcode.com/problems/palindromic-substrings
'''

class Solution:
    # pylint: disable-next=invalid-name
    def countSubstrings(self, s: str) -> int:
        '''
        I didn't come up with the algorithm. See Manacher's algorithm
        '''
        if len(s) <= 1:
            return 1
        n = 2 * len(s) + 1
        dp = [0] * n
        center = 0
        right = 0
        for i in range(n):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while (i - dp[i] > 0 and i + dp[i] < n - 1) and \
                (((i + dp[i] + 1) % 2 == 0) or \
                    ((s[(i - dp[i] - 1) // 2]) == (s[(i + dp[i] + 1) // 2]))):
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
        return sum(map(lambda lpc: lpc // 2 + lpc % 2, dp))
