class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True if cur.endOfWord else False
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for pre in prefix:
            if pre in cur.children:
                cur = cur.children[pre]
            else:
                return False
        return True
        
        