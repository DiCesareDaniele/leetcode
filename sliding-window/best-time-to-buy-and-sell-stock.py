'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''

class Solution:
    # pylint: disable-next=invalid-name
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit
