'''
https://leetcode.com/problems/decode-ways
'''

class Solution:
    # pylint: disable-next=invalid-name
    def numDecodings(self, s: str) -> int:
        '''
        DP[i] = (DP[i - 1] if s[i] != "0" else 0) + (DP[i - 2] if 10 <= int(s[i-2:i] <= 26 else 0)
        '''
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        i = 1
        j = 1
        for k in range(2, len(s) + 1):
            tmp = 0
            one = int(s[k - 1])
            two = int(s[k - 2:k])
            if one != 0:
                tmp += j
            if 10 <= two <= 26:
                tmp += i
            i = j
            j = tmp
        return j
