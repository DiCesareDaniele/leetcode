'''
https://leetcode.com/problems/longest-substring-without-repeating-characters
'''

class Solution:
    # pylint: disable-next=invalid-name
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        last_idx = 0
        chars = {}
        for i, c in enumerate(s):
            if c in chars:
                j = chars[c]
                max_l = max(max_l, i - last_idx)
                last_idx = max(last_idx, j + 1)
            chars[c] = i
        return max(max_l, len(s) - last_idx)
