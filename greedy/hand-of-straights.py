'''
https://leetcode.com/problems/hand-of-straights
'''

from collections import Counter

class Solution:
    # pylint: disable-next=invalid-name
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)

        for card in sorted(freq):
            f = freq[card]
            if f == 0:
                continue
            for val in range(card, card + groupSize):
                if val not in freq:
                    return False
                freq[val] -= f
                if freq[val] < 0:
                    return False
        return True
