class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.least_recent = None