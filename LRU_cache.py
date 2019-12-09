#Implementation building LRU Cache completely from Scratch

class Node:
    def __init__(self, val=0, key=0):
        self.val = val
        self.storage_key = key
        self.next = None
        self.prev = None


class DoubleLinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node

    def pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.usage_list = DoubleLinkedList()
        self.size = 0
        
        
    def get(self, key: int) -> int:
        # retrieve key value from storage
        if key not in self.storage:
            return -1
        node = self.storage[key]
        # extract value from node
        # remove node from current position in dll
        self.usage_list.pop_node(node)
        # append it to end of dll in most recently used postion
        self.usage_list.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # create node of value
        if key in self.storage:
            self.storage[key].val = value
            self.usage_list.pop_node(self.storage[key])
            self.usage_list.pop_node(self.storage[key])
        else:
            node = Node(value, key)
            self.usage_list.append(node)
            self.storage[key] = node
            if len(self.storage) > self.capacity:
                last_key = self.usage_list.head.next.storage_key
                self.storage.pop(last_key)
                self.usage_list.pop_node(self.usage_list.head.next)        
