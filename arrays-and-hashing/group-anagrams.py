'''
https://leetcode.com/problems/group-anagrams
'''

from collections import defaultdict

class Solution:
    # pylint: disable-next=invalid-name
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def signature(word: str) -> tuple[int]:
            sig = [0] * 26
            for c in word:
                sig[ord(c) - ord("a")] += 1
            return tuple(sig)
        groups = defaultdict(list)
        for s in strs:
            sig = signature(s)
            groups[sig].append(s)
        return list(groups.values())
