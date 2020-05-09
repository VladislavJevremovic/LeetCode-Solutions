# https://leetcode.com/problems/lru-cache/

class DoublyLinkedNode(): 
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList(): 
    def __init__(self):
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

    def move_node_to_head(self, node):
        self.remove_node(node)
        self.add_node_to_head(node)

    def pop_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        
        return res
            
class LRUCache():
    def __init__(self, capacity):
        self.list = DoublyLinkedList()
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        
    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.list.move_node_to_head(node)

        return node.value

    def put(self, key, value):
        node = self.cache.get(key, None)
        if not node: 
            new_node = DoublyLinkedNode(key, value)
            
            self.cache[key] = new_node
            self.list.add_node_to_head(new_node)

            self.size += 1
            if self.size > self.capacity:
                tail = self.list.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.list.move_node_to_head(node)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
