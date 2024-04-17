'''
https://leetcode.com/problems/car-fleet
'''

class Solution:
    # pylint: disable-next=invalid-name
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        arrival_time = ((target - p) / s for p, s in sorted(zip(position, speed), reverse=True))
        res = 0
        curr = 0
        for t in arrival_time:
            if curr < t:
                curr = t
                res += 1
        return res
