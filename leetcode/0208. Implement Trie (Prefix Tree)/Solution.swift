// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
    var value: Character?
    var children: [Character: TrieNode] = [:]
    var isTerminating = false

    init(value: Character? = nil) {
        self.value = value
    }

    func add(value: Character) {
        guard children[value] == nil else {
            return
        }
        children[value] = TrieNode(value: value)
    }
}

class Trie {
    private let root: TrieNode

    init() {
        root = TrieNode()
    }
}

extension Trie {
    func insert(_ word: String) {
        guard !word.isEmpty else { return }

        var currentNode = root
        for character in word.lowercased() {
            if let childNode = currentNode.children[character] {
                currentNode = childNode
            } else {
                currentNode.add(value: character)
                currentNode = currentNode.children[character]!
            }
        }

        guard !currentNode.isTerminating else { return }
        currentNode.isTerminating = true
    }

    func search(_ word: String) -> Bool {
        guard !word.isEmpty else { return false }

        var currentNode = root
        for character in word.lowercased() {
            guard let childNode = currentNode.children[character] else { return false }
            currentNode = childNode
        }

        return currentNode.isTerminating
    }

    func startsWith(_ prefix: String) -> Bool {
        guard !prefix.isEmpty else { return false }

        var currentNode = root
        for character in prefix.lowercased() {
            guard let childNode = currentNode.children[character] else { return false }
            currentNode = childNode
        }

        return true
    }
}

let trie = Trie()
trie.insert("apple")
assert(trie.search("apple") == true)
assert(trie.search("app") == false)
assert(trie.startsWith("app") == true)
trie.insert("app")
assert(trie.search("app") == true)
