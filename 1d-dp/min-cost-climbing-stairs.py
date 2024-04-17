'''
https://leetcode.com/problems/min-cost-climbing-stairs
'''

class Solution:
    # pylint: disable-next=invalid-name
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        '''
        DP[i] = cost[i] + min(DP[i - 1], DP[i - 2])
        '''
        i = cost[0]
        j = cost[1]
        for k in range(2, len(cost)):
            tmp = j
            j = cost[k] + min(i, j)
            i = tmp
        return min(i, j)
