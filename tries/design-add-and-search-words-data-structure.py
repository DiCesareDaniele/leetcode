'''
https://leetcode.com/problems/design-add-and-search-words-data-structure
'''

class WordDictionary:
    children: dict[str, 'WordDictionary']
    terminal: bool

    def __init__(self):
        self.children = {}
        self.terminal = False

    # pylint: disable-next=invalid-name
    def addWord(self, word: str) -> None:
        par = self
        for c in word:
            if c not in par.children:
                par.children[c] = WordDictionary()
            par = par.children[c]
        par.terminal = True

    def search(self, word: str) -> bool:
        def search_helper(node: WordDictionary, i: int) -> bool:
            if i == len(word):
                return node.terminal
            if word[i] == ".":
                for child in node.children.values():
                    if search_helper(child, i + 1):
                        return True
                return False
            if word[i] not in node.children:
                return False
            return search_helper(node.children[word[i]], i + 1)
        return search_helper(self, 0)
