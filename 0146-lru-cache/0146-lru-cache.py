class Node:
    def __init__(self, x: int, y: int, nex = None, prev = None):
        self.key = x
        self.value = y
        self.next = nex
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.actual_cap = 0
        self.mapping = {}
        self.LRU = None
        self.MRU = None

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.put(key, self.mapping[key].value)
            return self.mapping[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            current_node = self.mapping[key]
            if current_node is self.MRU:
                self.MRU.value = value
            elif current_node is self.LRU:
                self.LRU.next.prev = None
                self.LRU = self.LRU.next
                self.MRU.next = current_node
                current_node.prev = self.MRU
                self.MRU = current_node
                self.MRU.next = None
                self.MRU.value = value
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.MRU.next = current_node
                current_node.prev = self.MRU
                self.MRU = self.MRU.next
                self.MRU.next = None
                self.MRU.value = value
        elif self.actual_cap == 0:
            self.LRU = Node(key, value)
            self.MRU = self.LRU
            self.mapping[key] = self.LRU
            self.actual_cap += 1
        elif self.actual_cap < self.capacity:
            current_node = Node(key, value, prev=self.MRU)
            self.MRU.next = current_node
            self.MRU = current_node
            self.mapping[key] = current_node
            self.actual_cap += 1
        elif self.actual_cap == self.capacity:
            if self.capacity == 1:
                self.mapping.pop(self.LRU.key)
                self.LRU.key = key
                self.LRU.value = value
                self.mapping[key] = self.LRU
            else:
                self.mapping.pop(self.LRU.key)
                self.LRU = self.LRU.next
                self.LRU.prev = None
                self.MRU.next = Node(key, value, prev=self.MRU)
                self.MRU = self.MRU.next
                self.mapping[key] = self.MRU
		

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
