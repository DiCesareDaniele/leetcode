'''
https://leetcode.com/problems/longest-repeating-character-replacement
'''

class Solution:
    # pylint: disable-next=invalid-name
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        for c in set(s):
            low = 0
            high = 0
            ks = k
            while high < len(s):
                if s[high] != c and ks == 0:
                    max_l = max(max_l, high - low - 1)
                    if s[low] != c:
                        ks += 1
                    low += 1
                elif s[high] != c:
                    high += 1
                    ks -= 1
                else:
                    high += 1
            max_l = max(max_l, high - low - 1)
        return max_l
