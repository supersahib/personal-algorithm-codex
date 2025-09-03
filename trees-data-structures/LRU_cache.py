"""
Algorithm: LRU Cache (Least Recently Used)
Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
Category: Trees & Data Structures - Cache

Description:
    Cache with fixed capacity that evicts least recently used items
    Uses hashmap for O(1) lookup and doubly linked list for O(1) reordering

Use Cases:
    - Operating system page replacement
    - Database buffer pools
    - Web application caching
    - CDN cache management

LeetCode Problems:
    - Problem #146: LRU Cache
    - Problem #460: LFU Cache (variation)
"""

class Node:
    """
    Doubly linked list node for LRU cache
    """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize cache with given capacity
        
        Args:
            capacity: Maximum number of key-value pairs
        """
        self.capacity = capacity
        self.cache = {}  # key -> node mapping
        
        # Dummy head and tail for easier manipulation
        self.head = Node()  # Most recently used
        self.tail = Node()  # Least recently used
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_head(self, node):
        """
        Add node right after head (mark as most recently used)
        
        Time: O(1)
        """
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        tmp.prev = node
        node.next = tmp
    
    def _remove_node(self, node):
        """
        Remove node from its current position
        
        Time: O(1)
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """
        Move existing node to head (mark as recently used)
        
        Time: O(1)
        """
        self._remove_node(node)
        self._add_to_head(node)
        
    
    def _remove_tail(self):
        """
        Remove least recently used node (right before tail)
        
        Time: O(1)
        Returns: Removed node
        """
        
        node_to_rem = self.tail.prev
        self._remove_node(node_to_rem)
        return node_to_rem
    
    def get(self, key: int) -> int:
        """
        Get value for key if it exists
        
        Args:
            key: Key to look up
            
        Returns:
            Value if key exists, -1 otherwise
            
        Time: O(1)
        """
        if key not in self.cache:
            return -1
        
        self._move_to_head(self.cache[key])
        return self.cache[key].value

    
    def put(self, key: int, value: int) -> None:
        """
        Add or update key-value pair
        
        Args:
            key: Key to insert/update
            value: Value to store
            
        Time: O(1)
        """
        if key in self.cache:
            self.cache[key].value = value
            self._move_to_head(self.cache[key])
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                removed = self._remove_tail()
                del self.cache[removed.key]
            self._add_to_head(node)
            self.cache[key] = node

# Example usage and test cases
if __name__ == "__main__":
    # Test Case 1: Basic operations
    lru = LRUCache(2)
    
    lru.put(1, 1)  # cache is {1=1}
    lru.put(2, 2)  # cache is {1=1, 2=2}
    print(lru.get(1))  # returns 1, cache is {2=2, 1=1}
    
    lru.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    print(lru.get(2))  # returns -1 (not found)
    
    lru.put(4, 4)  # evicts key 1, cache is {3=3, 4=4}
    print(lru.get(1))  # returns -1
    print(lru.get(3))  # returns 3
    print(lru.get(4))  # returns 4
    
    # Test Case 2: Update existing key
    lru2 = LRUCache(2)
    lru2.put(2, 1)
    lru2.put(2, 2)  # update value
    print(lru2.get(2))  # should return 2
    
    # Expected output:
    # 1
    # -1
    # -1
    # 3
    # 4
    # 2