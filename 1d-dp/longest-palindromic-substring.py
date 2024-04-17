'''
https://leetcode.com/problems/longest-palindromic-substring
'''

class Solution:
    # pylint: disable-next=invalid-name
    def longestPalindrome(self, s: str) -> str:
        '''
        I didn't come up with the algorithm. See Manacher's algorithm
        '''
        if len(s) <= 1:
            return s
        n = 2 * len(s) + 1
        dp = [0] * n
        center = 0
        right = 0
        max_length = 0
        max_center = 0
        for i in range(n):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while (i - dp[i] > 0 and i + dp[i] < n - 1) and \
                (((i + dp[i] + 1) % 2 == 0) or \
                    ((s[(i - dp[i] - 1) // 2]) == (s[(i + dp[i] + 1) // 2]))):
                dp[i] += 1
            if dp[i] > max_length:
                max_length = dp[i]
                max_center = i
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
        start = (max_center - max_length) // 2
        end = start + max_length
        return s[start:end]
