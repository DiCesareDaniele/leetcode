'''
https://leetcode.com/problems/word-break
'''

class Solution:
    # pylint: disable-next=invalid-name
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        DP[i] = DP[i - len(w)] and s[i - len(w):i] == w
        '''
        def word_break_helper(i: int, cache: list[bool | None]) -> bool:
            if i == 0:
                return True
            if cache[i] is not None:
                return cache[i]
            for w in wordDict:
                if i < len(w):
                    continue
                if s[i - len(w):i] != w:
                    continue
                wb = word_break_helper(i - len(w), cache)
                cache[i] = wb
                if wb:
                    return True
            return False
        cache = [None] * (len(s) + 1)
        return word_break_helper(len(s), cache)
