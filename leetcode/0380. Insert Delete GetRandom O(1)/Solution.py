# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list) # value: insert_position
        self.list.append(val)
        
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        last_element = self.list[-1]
        index_of_val = self.dict[val]
        self.list[index_of_val] = last_element # move last element to val's position
        self.dict[last_element] = index_of_val # and update dict accordingly
        
        self.list.pop() # effectively shrink the list, popped may not be val
        del self.dict[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


randomSet = RandomizedSet()
assert randomSet.insert(1) == True
assert randomSet.remove(2) == False
assert randomSet.insert(2) == True
assert randomSet.getRandom() in [1, 2]
assert randomSet.remove(1) == True
assert randomSet.insert(2) == False
assert randomSet.getRandom() == 2
