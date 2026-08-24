class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        #MRU -> right
        #LRU -> left
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def insert_to_right(self, node) -> None:
        prev_MRU = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = prev_MRU
        prev_MRU.next = node
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_to_right(node)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        node = Node(key,value)
        self.cache[key] = node
        self.insert_to_right(node)
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
            
