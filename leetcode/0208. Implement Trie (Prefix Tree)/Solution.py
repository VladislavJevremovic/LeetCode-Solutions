# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = defaultdict(Trie.TrieNode) # {char: TrieNode}
            self.is_leaf = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children[c] # creates child if None
        current.is_leaf = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            current = current.children.get(c) # don't create child if None
            if not current:
                return False
        
        return current.is_leaf

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            current = current.children.get(c) # don't create child if None
            if not current:
                return False
        
        return True

trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True