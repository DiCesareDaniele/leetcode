'''
https://leetcode.com/problems/permutation-in-string
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        i = 0
        while i + len(s1) <= len(s2):
            tmp_count = {}
            for j in range(i, i + len(s1)):
                c = s2[j]
                if c not in s1_count:
                    i = j + 1
                    break
                if tmp_count.get(c, 0) >= s1_count[c]:
                    while s2[i] != c:
                        i += 1
                    i += 1
                    break
                tmp_count[c] = tmp_count.get(c, 0) + 1
            else:
                return True
        return False
