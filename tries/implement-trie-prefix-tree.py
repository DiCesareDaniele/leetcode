'''
https://leetcode.com/problems/implement-trie-prefix-tree
'''

class Trie:
    children: dict[str, 'Trie']
    terminal: bool

    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word: str) -> None:
        par = self
        for c in word:
            if c not in par.children:
                par.children[c] = Trie()
            par = par.children[c]
        par.terminal = True

    def search(self, word: str) -> bool:
        par = self
        for c in word:
            if c not in par.children:
                return False
            par = par.children[c]
        return par.terminal

    # pylint: disable-next=invalid-name
    def startsWith(self, prefix: str) -> bool:
        par = self
        for c in prefix:
            if c not in par.children:
                return False
            par = par.children[c]
        return True
