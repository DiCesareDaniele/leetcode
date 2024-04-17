'''
https://leetcode.com/problems/merge-triplets-to-form-target-triplet
'''

class Solution:
    # pylint: disable-next=invalid-name
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        tl = len(target)
        to_merge = [0] * tl
        for t in triplets:
            if all(t[i] <= target[i] for i in range(tl)):
                for i in range(tl):
                    if t[i] == target[i]:
                        to_merge[i] = t[i]
                if to_merge == target:
                    return True
        return False
