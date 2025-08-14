# Sahib's Algorithm Codex

> My personal collection of algorithm implementations and explorations as I journey through computer science fundamentals and advanced techniques

## About

This repository serves as my personal algorithm codex - a growing collection of algorithms I've studied, implemented, and understood deeply. Each implementation includes my notes, learnings, and practical applications I've discovered along the way.

### Why This Repository?

- **Personal Learning Journey**: Document my understanding of fundamental algorithms
- **Reference Implementation**: Clean, well-commented code I can refer back to
- **Knowledge Consolidation**: Writing implementations helps solidify concepts
- **Interview Preparation**: Build a comprehensive toolkit for technical interviews
- **Continuous Growth**: Expand my knowledge into advanced algorithmic territories


## Completed Algorithms
- [x] **Radix Sort** - Non-comparative
- [x] **Bucket Sort** - Distribution sort

## To-Do Algorithms 
### Sorting & Searching
- [ ] **Binary Search** - And variations
- [ ] **QuickSort** - Randomized pivot
- [ ] **MergeSort** - Stable sorting
- [ ] **HeapSort** - In-place sorting
- [x] **Radix Sort** - Non-comparative
- [ ] **Counting Sort** - Integer sorting
- [x] **Bucket Sort** - Distribution sort
- [ ] **QuickSelect** - Kth element

### String Algorithms
- [ ] **Rabin-Karp** - Rolling hash pattern matching
- [ ] **KMP (Knuth-Morris-Pratt)** - Efficient string matching with failure function
- [ ] **Boyer-Moore** - Efficient string matching
- [ ] **Z-Algorithm** - Pattern matching alternative
- [ ] **Aho-Corasick** - Multiple pattern matching
- [ ] **Manacher's Algorithm** - Finding palindromes in linear time
- [ ] **Suffix Array** - String processing
- [ ] **Suffix Tree** - Advanced string operations
- [ ] **Trie** - Prefix tree
- [ ] **Rolling Hash Applications** - Various uses
- [ ] **Burrows-Wheeler Transform** - Compression preprocessing

### Graph Algorithms
- [ ] **DFS (Depth-First Search)** - Graph traversal
- [ ] **BFS (Breadth-First Search)** - Level-order traversal
- [ ] **Dijkstra's Algorithm** - Single source shortest path
- [ ] **Bellman-Ford** - Handles negative edges
- [ ] **Floyd-Warshall** - All pairs shortest path
- [ ] **A* Search** - Heuristic pathfinding
- [ ] **Union-Find** - Disjoint set operations
- [ ] **Kruskal's Algorithm** - MST using edges
- [ ] **Prim's Algorithm** - MST using vertices
- [ ] **Topological Sort** - DAG ordering
- [ ] **Tarjan's Algorithm** - Strongly connected components
- [ ] **Kosaraju's Algorithm** - Alternative SCC
- [ ] **Articulation Points & Bridges** - Critical connections
- [ ] **Ford-Fulkerson** - Maximum flow
- [ ] **Edmonds-Karp** - BFS-based max flow
- [ ] **Dinic's Algorithm** - Faster max flow
- [ ] **Hungarian Algorithm** - Assignment problem
- [ ] **Johnson's Algorithm** - All pairs shortest path
- [ ] **Hierholzer's Algorithm** - Eulerian path
- [ ] **Cycle Detection** - Finding cycles

### Dynamic Programming
- [ ] **Kadane's Algorithm** - Maximum subarray sum
- [ ] **0/1 Knapsack** - Classic optimization
- [ ] **Unbounded Knapsack** - Unlimited items
- [ ] **Longest Common Subsequence** - String comparison
- [ ] **Longest Increasing Subsequence** - O(n log n) solution
- [ ] **Edit Distance** - Levenshtein distance
- [ ] **Coin Change** - Minimum coins problem
- [ ] **Matrix Chain Multiplication** - Optimization problem
- [ ] **Palindrome Partitioning** - String splitting
- [ ] **Rod Cutting** - Maximum profit
- [ ] **Egg Dropping** - Classic puzzle
- [ ] **Word Break** - String segmentation
- [ ] **Bitmask DP** - Subset problems
- [ ] **Digit DP** - Number theory problems
- [ ] **DP on Trees** - Tree optimization

### Trees & Data Structures
- [ ] **Binary Tree Traversals** - All variations
- [ ] **Binary Search Tree** - Operations
- [ ] **AVL Tree** - Self-balancing BST
- [ ] **Red-Black Tree** - Another balancing approach
- [ ] **B-Tree** - Database indexing
- [ ] **Segment Tree** - Range queries
- [ ] **Fenwick Tree (BIT)** - Prefix sums
- [ ] **Heap/Priority Queue** - Min and Max
- [ ] **LRU Cache** - Eviction policy
- [ ] **LFU Cache** - Frequency-based eviction
- [ ] **Treap** - Randomized BST
- [ ] **Skip List** - Probabilistic structure
- [ ] **Persistent Data Structures** - Version history

### Mathematical Algorithms
- [ ] **Euclidean Algorithm** - GCD
- [ ] **Extended Euclidean Algorithm** - Modular inverse
- [ ] **Sieve of Eratosthenes** - Prime generation
- [ ] **Miller-Rabin** - Primality testing
- [ ] **Fast Fourier Transform** - Polynomial multiplication
- [ ] **Chinese Remainder Theorem** - Congruences
- [ ] **Graham Scan** - Convex hull
- [ ] **Line Sweep Algorithm** - Geometric problems
- [ ] **Karatsuba Multiplication** - Fast multiplication
- [ ] **Matrix Exponentiation** - Fast computation


### System Design Algorithms
- [ ] **Consistent Hashing** - Load distribution
- [ ] **Bloom Filter** - Membership testing
- [ ] **Count-Min Sketch** - Frequency estimation
- [ ] **HyperLogLog** - Cardinality estimation
- [ ] **Reservoir Sampling** - Stream sampling
- [ ] **Rate Limiting** - Token bucket, sliding window
- [ ] **Raft Consensus** - Distributed agreement
- [ ] **Vector Clocks** - Causality tracking
- [ ] **Gossip Protocol** - Information dissemination
- [ ] **Merkle Tree** - Data verification

### Randomized & Probabilistic
- [ ] **Monte Carlo Methods** - Probabilistic solutions
- [ ] **Las Vegas Algorithms** - Always correct
- [ ] **Fisher-Yates Shuffle** - Random permutation
- [ ] **Rejection Sampling** - Distribution generation
- [ ] **MinHash** - Similarity estimation
- [ ] **SimHash** - Near-duplicate detection

### Compression & Encoding
- [ ] **Huffman Coding** - Variable-length codes
- [ ] **LZ77/LZ78** - Dictionary compression
- [ ] **Run-Length Encoding** - Simple compression
- [ ] **Arithmetic Coding** - Entropy encoding

### Game Theory & Optimization
- [ ] **Minimax** - Game tree evaluation
- [ ] **Alpha-Beta Pruning** - Search optimization
- [ ] **Monte Carlo Tree Search** - Game AI
- [ ] **Genetic Algorithm** - Evolutionary approach
- [ ] **Simulated Annealing** - Probabilistic optimization

## Implementation Template

Each algorithm implementation follows this structure:

```python
"""
Algorithm: [Name]
Time Complexity: O(?)
Space Complexity: O(?)
Category: [Category]

Description:
    Detailed explanation of how the algorithm works

Use Cases:
    - Real world application 1
    - Real world application 2

LeetCode Problems:
    - Problem #XXX: [Name]
    - Problem #YYY: [Name]
"""

class Algorithm:
    def __init__(self):
        """Initialize any necessary data structures"""
        pass
    
    def solve(self, input_data):
        """
        Main algorithm implementation
        
        Args:
            input_data: Description
            
        Returns:
            result: Description
            
        Time: O(?)
        Space: O(?)
        """
        pass

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"input": ..., "expected": ...},
        {"input": ..., "expected": ...}
    ]
    
    algo = Algorithm()
    for test in test_cases:
        result = algo.solve(test["input"])
        assert result == test["expected"]
```

## Resources

### Books
- "Introduction to Algorithms" - CLRS
- "Algorithm Design" - Kleinberg & Tardos
- "The Algorithm Design Manual" - Skiena
- "Competitive Programming 3" - Halim & Halim

### Online Platforms
- **LeetCode** - Practice problems
- **Codeforces** - Competitive programming
- **GeeksforGeeks** - Explanations
- **CP-Algorithms** - Detailed implementations

### Visualization Tools
- **VisuAlgo** - Algorithm animations
- **Algorithm Visualizer** - Interactive learning
- **CS.usfca.edu** - Data structure visualizations

## Notes

Each algorithm folder contains a `notes.md` file where I document:
- Key insights and gotchas
- Common pitfalls and edge cases
- Optimization techniques
- Related problems and variations
- Implementation tips

## Running Tests

```bash
# Run all tests
python -m pytest

# Run tests for specific category
python -m pytest string-algorithms/

# Run with coverage
python -m pytest --cov=.
```