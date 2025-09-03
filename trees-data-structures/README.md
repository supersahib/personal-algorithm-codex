# Trees & Data Structures

Exploring tree-based data structures and advanced data organization techniques for efficient operations.

## Core Concepts

### Tree Fundamentals
Binary trees, BSTs, balanced trees, and tree traversal algorithms that form the foundation of hierarchical data organization.

### Self-Balancing Trees
AVL, Red-Black, and B-Trees that maintain balance for guaranteed O(log n) operations.

### Specialized Structures
Tries for string operations, segment trees for range queries, and hybrid structures combining multiple techniques.

### Cache Structures
LRU, LFU, and other eviction policies implemented with combinations of hashmaps and linked lists for O(1) operations.

# Implemented Algorithms

## LRU Cache (Least Recently Used)

Implements a cache with O(1) get/put operations using a hashmap and doubly linked list combination.

**Components:**
- **HashMap**: Maps keys to node references for O(1) access
- **Doubly Linked List**: Maintains usage order (most recent at head, least recent at tail)
- **Node Structure**: Contains key, value, and prev/next pointers
- **Capacity Management**: Evicts LRU item when capacity exceeded

**Operations:**
1. **Get(key)**: 
   - Check if key exists in hashmap
   - If found, move node to head (mark as recently used)
   - Return value
2. **Put(key, value)**:
   - If key exists, update value and move to head
   - If new key, create node and add to head
   - If over capacity, remove tail node (LRU)

**Complexity:**
- Get: O(1) - HashMap lookup + linked list manipulation
- Put: O(1) - HashMap operation + linked list manipulation
- Space: O(capacity)

**Key Insights:**
- HashMap provides fast key lookup
- Doubly linked list maintains temporal ordering
- Moving nodes to head marks them as recently used
- Tail always contains LRU item for eviction
- Dummy head/tail nodes simplify edge cases

**Use Cases:**
- Operating system page replacement
- Database buffer pools
- Application-level caching (Redis, Memcached)
- CDN cache management
- Mobile app data caching

**Variations:**
- **LFU (Least Frequently Used)**: Track frequency instead of recency
- **ARC (Adaptive Replacement Cache)**: Combines recency and frequency
- **2Q Cache**: Uses two queues for better scan resistance
- **FIFO Cache**: Simple queue-based eviction

**LeetCode Problems:**
- #146: LRU Cache
- #460: LFU Cache
- #432: All O(1) Data Structure

## TODO

### Binary Trees
- [ ] **Tree Traversals**: Inorder, Preorder, Postorder (recursive & iterative)
- [ ] **Level Order Traversal**: BFS on trees
- [ ] **Morris Traversal**: O(1) space tree traversal
- [ ] **Lowest Common Ancestor**: Finding LCA in binary trees

### Binary Search Trees
- [ ] **BST Operations**: Insert, delete, search
- [ ] **Validate BST**: Check if tree is valid BST
- [ ] **BST Iterator**: In-order iterator design
- [ ] **Kth Smallest**: Finding kth smallest in BST

### Balanced Trees
- [ ] **AVL Tree**: Self-balancing with rotations
- [ ] **Red-Black Tree**: Less strict balancing
- [ ] **B-Tree**: Multi-way search tree for databases
- [ ] **B+ Tree**: Variant optimized for disk access

### Heaps & Priority Queues
- [ ] **Binary Heap**: Min/Max heap implementation
- [ ] **Heapify**: Building heap from array
- [ ] **Heap Sort**: In-place sorting
- [ ] **K-way Merge**: Using heap for multiple sorted streams
- [ ] **Fibonacci Heap**: Advanced heap with better amortized complexity

### Advanced Trees
- [ ] **Segment Tree**: Range queries and updates
- [ ] **Fenwick Tree (BIT)**: Efficient prefix sums
- [ ] **Trie**: Prefix tree for strings
- [ ] **Suffix Tree**: Pattern matching
- [ ] **Treap**: Randomized BST
- [ ] **Splay Tree**: Self-adjusting BST

### Specialized Data Structures
- [ ] **Union-Find**: Disjoint set operations
- [ ] **Skip List**: Probabilistic alternative to balanced trees
- [ ] **Bloom Filter**: Probabilistic membership testing
- [ ] **Count-Min Sketch**: Frequency estimation

### Cache Implementations
- [ ] **LFU Cache**: Least frequently used eviction
- [ ] **Time-Based Cache**: TTL-based expiration
- [ ] **Write-Through/Write-Back Cache**: Different write policies