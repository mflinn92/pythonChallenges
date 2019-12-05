class Node:
    def __init__(self, val=0, key=0):
        self.val = val
        self.storage_key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        # retrieve key value from storage
        if key not in self.storage:
            return -1
        node = self.storage[key]
        # extract value from node
        # remove node from current position in dll
        self._remove(node)
        # append it to end of dll in most recently used postion
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # create node of value
        if key in self.storage:
            self.storage[key].val = value
            self._remove(self.storage[key])
            self._append(self.storage[key])
        else:
            node = Node(value, key)
            self._append(node)
            self.storage[key] = node
            if len(self.storage) > self.capacity:
                last_key = self.head.storage_key
                self.storage.pop(last_key)
                self._remove(self.head)        
            
    def _append(self, node):
        temp = self.tail.prev
        node.next = self.tail
        
            
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
