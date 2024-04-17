'''
https://leetcode.com/problems/minimum-window-substring
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        i = 0
        j = 0
        matched = 0
        min_w_len = len(s) + 1
        min_w = ""
        while j < len(s):
            c = s[j]
            if c not in t_count:
                j += 1
                continue
            t_count[c] -= 1
            if t_count[c] == 0:
                matched += 1
                if matched == len(t_count):
                    while s[i] not in t_count or t_count[s[i]] < 0:
                        if s[i] in t_count:
                            t_count[s[i]] += 1
                        i += 1
                    if j + 1 - i < min_w_len:
                        min_w_len = j + 1 - i
                        min_w = s[i:j + 1]
                    t_count[s[i]] += 1
                    i += 1
                    matched -= 1
            j += 1
        return min_w
