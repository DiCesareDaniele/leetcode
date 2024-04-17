'''
https://leetcode.com/problems/partition-labels
'''

class Solution:
    # pylint: disable-next=invalid-name
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        labels = []
        last_char_table = {c: i for i, c in enumerate(s)}
        start = 0
        end = last_char_table[s[0]]
        i = 0
        while i < n:
            while i <= end:
                if last_char_table[s[i]] > end:
                    end = last_char_table[s[i]]
                    if end == n - 1:
                        break
                i += 1
            labels.append(end - start + 1)
            if end == n - 1:
                break
            start = i
            end = last_char_table[s[i]]
        return labels
