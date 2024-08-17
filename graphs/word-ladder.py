'''
https://leetcode.com/problems/word-ladder
'''

from collections import defaultdict, deque

class Solution:
    # pylint: disable-next=invalid-name
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        word_map = defaultdict(list)
        for w in word_list:
            for i in range(len(w)):
                kw = w[:i] + "*" + w[i+1:]
                word_map[kw].append(w)
        distances = {}
        def bfs():
            queue = deque()
            queue.append(begin_word)
            distances[begin_word] = 0
            while len(queue) > 0:
                word = queue.popleft()
                for i in range(len(word)):
                    kw = word[:i] + "*" + word[i+1:]
                    for w in word_map[kw]:
                        if not w in distances:
                            distances[w] = distances[word] + 1
                            queue.append(w)
        bfs()
        if end_word not in distances:
            return 0
        return 1 + distances[end_word]
