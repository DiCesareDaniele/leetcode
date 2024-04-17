'''
https://leetcode.com/problems/gas-station
'''

class Solution:
    # pylint: disable-next=invalid-name
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        tot_gas = 0
        tot_cost = 0
        curr_gas = 0
        start = 0
        for i in range(n):
            tot_gas += gas[i]
            tot_cost += cost[i]

            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0
        return start if tot_gas >= tot_cost else -1
