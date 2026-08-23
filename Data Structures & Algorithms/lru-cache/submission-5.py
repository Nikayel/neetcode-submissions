class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #right side -> MRU
        #left side -> LRU
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
    def insert(self, node) -> int:
        old_mru = self.right.prev
        old_mru.next = node
        self.right.prev = node
        node.prev = old_mru
        node.next = self.right
    def remove(self, node)-> int:
        node.next.prev = node.prev
        node.prev.next = node.next
    def get(self, key:int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]

