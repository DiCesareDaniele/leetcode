'''
https://leetcode.com/problems/word-search-ii
'''

class Trie:
    children: dict[str, 'Trie']
    terminal: bool
    refs: int

    def __init__(self):
        self.children = {}
        self.terminal = False
        self.refs = 0

    def insert(self, word: str) -> None:
        par = self
        par.refs += 1
        for c in word:
            if c not in par.children:
                par.children[c] = Trie()
            par = par.children[c]
            par.refs += 1
        par.terminal = True

    def remove(self, word: str) -> None:
        par = self
        par.refs -= 1
        for c in word:
            if c in par.children:
                par = par.children[c]
                par.refs -= 1
        par.terminal = False

class Solution:
    # pylint: disable-next=invalid-name
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = Trie()
        for word in words:
            root.insert(word)
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        sol = []
        def exist_helper(i: int, j: int, trie: Trie, prefix: str) -> bool:
            if i >= m or j >= n or i < 0 or j < 0:
                return
            c = board[i][j]
            if visited[i][j] or c not in trie.children or trie.children[c].refs <= 0:
                return
            child = trie.children[c]
            prefix += c
            if child.terminal:
                sol.append(prefix)
                root.remove(prefix)
            visited[i][j] = True
            exist_helper(i + 1, j, child, prefix)
            exist_helper(i - 1, j, child, prefix)
            exist_helper(i, j + 1, child, prefix)
            exist_helper(i, j - 1, child, prefix)
            visited[i][j] = False
        for i in range(m):
            for j in range(n):
                exist_helper(i, j, root, "")
        return sol
