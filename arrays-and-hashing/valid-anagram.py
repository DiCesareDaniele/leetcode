'''
https://leetcode.com/problems/valid-anagram
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
