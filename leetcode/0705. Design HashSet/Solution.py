# https://leetcode.com/problems/design-hashset/

from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.hash_map = defaultdict(bool)

    def add(self, key: int) -> None:
        self.hash_map[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hash_map[key]

    def contains(self, key: int) -> bool:
        return self.hash_map[key]


hash_set = MyHashSet()
hash_set.add(1)
hash_set.add(2)
assert hash_set.contains(1) == True
assert hash_set.contains(3) == False
hash_set.add(2)
assert hash_set.contains(2) == True
hash_set.remove(2)
assert hash_set.contains(2) == False

hash_set = MyHashSet()
hash_set.add(9)
hash_set.remove(19)
hash_set.add(14)
hash_set.remove(19)
hash_set.remove(9)
hash_set.add(0)
hash_set.add(3)
hash_set.add(4)
hash_set.add(0)
hash_set.remove(9)
