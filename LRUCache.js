var Node = function(key, val) {
  this.val = val;
  this.key = key;
  this.next = null;
  this.prev = null;
}

var DoubleLinkedList = function() {
  this.head = new Node();
  this.tail = new Node();
  this.head.next = this.tail;
  this.tail.prev = this.head;
}
  
DoubleLinkedList.prototype.removeNode = function(node) {
  node.prev.next = node.next;
  node.next.prev = node.prev;
}
  
DoubleLinkedList.prototype.append = function(node) {
  const temp = this.tail.prev;
  temp.next = node;
  node.prev = temp;
  this.tail.prev = node;
  node.next = this.tail;
}

/**
* @param {number} capacity
*/
var LRUCache = function(capacity) {
  this.capacity = capacity
  this._map = {};
  this._storage = new DoubleLinkedList();
  this.size = 0;
};

/** 
* @param {number} key
* @return {number}
*/
LRUCache.prototype.get = function(key) {
  if (!this._map[key]) {
      return -1;
  }
  const target = this._map[key];
  this._storage.removeNode(target);
  this._storage.append(target);
  return target.val;
};

/** 
* @param {number} key 
* @param {number} value
* @return {void}
*/
LRUCache.prototype.put = function(key, value) {
  if (this._map[key]) {
    this._map[key].val = value;
    this._storage.removeNode(this._map[key]);
    this._storage.append(this._map[key]);
  } else {
    const node = new Node(key, value);
    this._map[key] = node;
    this._storage.append(node);
    this.size++;
    
    if (this.size > this.capacity) {
      const oldKey = this._storage.head.next.key;
      delete this._map[oldKey];
      this._storage.removeNode(this._storage.head.next);
      this.size--;
    }
  } 
};