'''
https://leetcode.com/problems/valid-palindrome/
'''

import re

class Solution:
    # pylint: disable-next=invalid-name
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", "", s.lower())
        return s == s[::-1]
