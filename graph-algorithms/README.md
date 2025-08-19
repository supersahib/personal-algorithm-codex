# Graph Algorithms

## Notes from Intro to Algorithms Book
 Chapters 22-26

### Representation of Graphs
- Two standard ways to represent graph `G = (V,E)`:
    - collection of adjancency lists
    - adjacency matrix

- **Adjacency-list** is usually method of choice
    - provides compact way to represent **sparse** graphs (those for which `|E|` is much less than `|V|^2`)
- **Adjacency matrix** preferred when graph is **dense**
    - When `|E|` is close to `|V|^2`
    - When we need to quickly tell if there is an edge connecting two given vertices
    - Space complexity: O(V²)

### Graph Implementation
```python
class Vertex:
    """Vertex with adjacency list as dictionary"""
    def __init__(self, key):
        self.id = key
        self.neighbors = {}  # neighbor_vertex -> weight

class Graph:
    """Graph using Vertex objects"""
    def __init__(self, directed=False):
        self.vertices = {}  # key -> Vertex object
        self.directed = directed
```

# Implemented Algorithms


## Breadth-first search
**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)

### Algorithm Overview
- Systematically explores edges of G to discover every vertex reachable from source `s`
- Expands the frontier between discovered and undiscovered vertices uniformly across the breadth
    - Discovers all vertices at distance `k` from `s` before discovering any vertices at distance `k+1`

#### Vertex Coloring (Conceptual)
- **White**: Undiscovered vertices
- **Gray**: Discovered but not fully explored (frontier)
- **Black**: Fully explored (all neighbors discovered)
- to keep track, BFS-search colors each vertex: white, gray, or black
    - all vertices start out white
    - becomes non-white when vertex is discovered first time
    - vertex is black when all vertices adjacent to it have been discovered
    - gray vertices may have some adjacent white vertices

![BFS algo](../images/BFS_algo.png)

### Implementation Variants

##### 1. Basic BFS Traversal
```python
def bfs_basic(self, start_key) -> List:
    """Returns vertices in BFS order"""
    # Key insight: Mark as visited when ADDING to queue
    # This prevents duplicates in queue
```

##### 2. Level-wise BFS
```python
def bfs_with_levels(self, start_key) -> List[List]:
    """Groups vertices by distance from start"""
    # Returns: [['A'], ['B', 'C'], ['D', 'E', 'F'], ...]
    # Process all nodes at current level before next
```

##### 3. Shortest Distances
```python
def bfs_shortest_distances(self, start_key) -> Dict[str, int]:
    """Returns distance from start to all reachable vertices"""
    # BFS guarantees shortest path in unweighted graphs
```

##### 4. Shortest Path
```python
def shortest_path(self, start_key, end_key) -> Optional[List]:
    """Finds shortest path between two vertices"""
    # Uses parent pointers to reconstruct path
    # Early termination when target found
```

#### Key Insights
1. **Queue vs Stack**: BFS uses queue (FIFO) vs DFS uses stack (LIFO)
2. **When to mark visited**: Always mark when adding to queue, not when processing
3. **Level boundaries**: `len(queue)` at start of iteration = nodes at current level
4. **Path reconstruction**: Track parent pointers, then walk backwards
5. **Shortest path property**: BFS finds shortest path in **unweighted** graphs

#### Applications
- Shortest path in unweighted graphs
- Finding connected components
- Testing bipartiteness
- Level-order traversal in trees
- Web crawling (limited depth)
- Social network analysis (degrees of separation)
- Puzzle solving (finding minimum moves)



# To Implement

### Depth-First Search (DFS)
- [ ] Recursive and iterative implementations
- [ ] Cycle detection
- [ ] Topological sort
- [ ] Connected components

### Shortest Path Algorithms
- [ ] Dijkstra's Algorithm (weighted graphs)
- [ ] Bellman-Ford (negative edges)
- [ ] Floyd-Warshall (all-pairs)

### Minimum Spanning Trees
- [ ] Kruskal's Algorithm
- [ ] Prim's Algorithm

### Advanced
- [ ] Strongly Connected Components (Kosaraju/Tarjan)
- [ ] Articulation Points & Bridges
- [ ] Network Flow (Ford-Fulkerson)