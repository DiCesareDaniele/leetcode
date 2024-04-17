'''
https://leetcode.com/problems/coin-change
'''

class Solution:
    # pylint: disable-next=invalid-name
    def coinChange(self, coins: list[int], amount: int) -> int:
        '''
        DP[a] = 1 + min(DP[a - coins[i]])
        '''
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a and dp[a - coin] != -1:
                    dp[a] = 1 + dp[a - coin] if dp[a] == -1 else min(dp[a], 1 + dp[a - coin])
        return dp[amount]
