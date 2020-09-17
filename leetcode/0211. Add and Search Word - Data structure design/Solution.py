# https://leetcode.com/problems/add-and-search-word-data-structure-design/

from collections import defaultdict


class WordDictionary:
    class Node:
        def __init__(self):
            self.children = defaultdict(WordDictionary.Node)  # {char: Node}
            self.is_leaf = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children[c]  # creates child if None
        current.is_leaf = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary.Node, level: int):
            if level == len(word):
                return node.is_leaf

            c = word[level]

            if c == ".":
                for child in node.children:
                    if dfs(node.children[child], level + 1):
                        return True

            if c in node.children:
                return dfs(node.children[c], level + 1)

            return False

        return dfs(self.root, 0)


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
assert wd.search("pad") == False
assert wd.search("bad") == True
assert wd.search(".ad") == True
assert wd.search("b..") == True
