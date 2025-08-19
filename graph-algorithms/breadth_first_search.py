"""
Algorithm: Breadth-First Search (BFS)
Time Complexity: O(V + E)
Space Complexity: O(V)
Category: Graph Traversal

Description:
    Level-by-level graph exploration using a queue
    Guarantees shortest path in unweighted graphs

Use Cases:
    - Shortest path in unweighted graphs
    - Level-order traversal
    - Connected components
    - Bipartite checking

LeetCode Problems:
    - Problem #102: Binary Tree Level Order Traversal
    - Problem #127: Word Ladder
    - Problem #785: Is Graph Bipartite?
    - #994: Rotting Oranges
    - #1091: Shortest Path in Binary Matrix
"""

from collections import deque
from typing import List, Dict, Set, Optional, Tuple

class Vertex:
    """
    Vertex class that maintains its own adjacency list
    """
    def __init__(self, key):
        self.id = key
        self.neighbors = {}  # neighbor_vertex -> weight
    
    def add_neighbor(self, neighbor, weight=1):
        """Add a neighbor with optional weight"""
        self.neighbors[neighbor] = weight
    
    def get_connections(self):
        """Return all connected vertices"""
        return self.neighbors.keys()
    
    def get_weight(self, neighbor):
        """Get weight of edge to neighbor"""
        return self.neighbors.get(neighbor, None)
    
    def __str__(self):
        return f"{self.id} -> {[x.id for x in self.neighbors]}"

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}   # key -> Vertex object
        self.num_vertices = 0
        self.directed = directed

    def add_vertex(self, key):
        if key not in self.vertices:
            self.num_vertices += 1
            new_vertex = Vertex(key)
            self.vertices[key] = new_vertex
            return new_vertex
        return None
    
    def add_edge(self, from_key, to_key, weight=1):
        """Add edge between two vertices"""
        # Add vertices if they don't exist
        if from_key not in self.vertices:
            self.add_vertex(from_key)
        if to_key not in self.vertices:
            self.add_vertex(to_key)
        
        # add edge from --> to
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)

        # if undirected, add edge to-->from
        if not self.directed:
            self.vertices[to_key].add_neighbor(self.vertices[from_key], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        """make graph iterable over vertices"""
        return iter(self.vertices.values())


class BFSTraversal:
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def bfs_basic(self, start_key) -> List:
        """
        Basic BFS that returns node keys in visit order
        
        Args:
            start_key: Starting vertex key (not Vertex object)
            
        Returns:
            List of vertex keys in BFS order
        """
        if start_key not in self.graph.vertices:
            return []

        start = self.graph.vertices[start_key]
        visited = set([start_key])  # Mark visited IMMEDIATELY
        queue = deque([start])
        result = []  # Simple list, not levels

        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex.id) 
            for neighbor_vertex in current_vertex.get_connections():
                if neighbor_vertex.id not in visited:
                    visited.add(neighbor_vertex.id)
                    queue.append(neighbor_vertex)
        return result


            
    def bfs_with_levels(self, start_key) -> List[List]:
        """
        BFS that groups vertex keys by their distance from start
        
        Args:
            start_key: Starting vertex key
            
        Returns:
            List of lists, where result[i] contains all vertex keys at distance i
            Example: [['A'], ['B', 'C'], ['D', 'E', 'F', 'G'], ['H']]
        """
        if start_key not in self.graph.vertices:
            return []
        
        start = self.graph.vertices[start_key]
        visited = set([start_key])
        queue = deque([start])
        levels = []
        
        while queue:
            current_level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                current_vertex = queue.popleft()
                current_level.append(current_vertex.id)

                for neighbor_vertex in current_vertex.get_connections():
                    if neighbor_vertex.id not in visited:
                        visited.add(neighbor_vertex.id)
                        queue.append(neighbor_vertex)
            levels.append(current_level)
            
        return levels

    def bfs_shortest_distances(self, start_key) -> Dict[str, int]:
        """
        BONUS: Return distance from start to all reachable vertices
        
        Returns:
            Dictionary mapping vertex_key -> distance
            Example: {'A': 0, 'B': 1, 'C': 1, 'D': 2, ...}
        """
        if start_key not in self.graph.vertices:
            return {}
        
        start = self.graph.vertices[start_key]
        visited = set([start_key])
        queue = deque([start])
        distances = {start_key: 0}
        
        while queue:
            current_vertex = queue.popleft()
            current_distance = distances[current_vertex.id]
            
            for neighbor_vertex in current_vertex.get_connections():
                if neighbor_vertex.id not in visited:
                    visited.add(neighbor_vertex.id)
                    queue.append(neighbor_vertex)
                    distances[neighbor_vertex.id] = current_distance + 1
        return distances
    
    def shortest_path(self, start_key, end_key) -> Optional[List]:
        """
        Find shortest path between start and end vertices
        
        Returns:
            Path as list of vertex keys, or None if no path exists
        """

        if start_key == end_key:
            return [start_key]
        
        start = self.graph.vertices[start_key]
        visited = set([start_key])
        queue = deque([start])
        parent = {start_key: None}
        
        
        while queue:
            current_vertex = queue.popleft()
            if current_vertex.id == end_key:
                path = []
                current = end_key
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path
            
            for neighbor_vertex in current_vertex.get_connections():
                if neighbor_vertex.id not in visited:
                    visited.add(neighbor_vertex.id)
                    queue.append(neighbor_vertex)
                    parent[neighbor_vertex.id] = current_vertex.id
        
        return None


if __name__ == "__main__":
    # Test Case 1: Tree structure
    print("=" * 50)
    print("TEST CASE 1: Tree Structure")
    print("=" * 50)
    
    g1 = Graph(directed=False)
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('D', 'H')
    ]
    for u, v in edges:
        g1.add_edge(u, v)
    
    bfs1 = BFSTraversal(g1)
    
    print("Graph structure:")
    print("       A")
    print("      / \\")
    print("     B   C")
    print("    /|   |\\")
    print("   D E   F G")
    print("  /")
    print(" H")
    print()
    
    print("Basic BFS from 'A':", bfs1.bfs_basic('A'))
    print("Expected:           ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")
    print()
    
    print("Levels from 'A':", bfs1.bfs_with_levels('A'))
    print("Expected:        [['A'], ['B', 'C'], ['D', 'E', 'F', 'G'], ['H']]")
    print()
    
    print("Distances from 'A':", bfs1.bfs_shortest_distances('A'))
    print("Expected:           {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2, 'G': 2, 'H': 3}")
    print()
    
    print("Path A -> H:", bfs1.shortest_path('A', 'H'))
    print("Expected:    ['A', 'B', 'D', 'H']")
    print()
    
    print("Path H -> G:", bfs1.shortest_path('H', 'G'))
    print("Expected:    ['H', 'D', 'B', 'A', 'C', 'G']")
    print()

    # Test Case 2: Cycle/Diamond structure
    print("=" * 50)
    print("TEST CASE 2: Graph with Cycles")
    print("=" * 50)
    
    g2 = Graph(directed=False)
    edges2 = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('C', 'D'),  # Diamond shape
        ('D', 'E'), ('B', 'E')   # Multiple paths to E
    ]
    for u, v in edges2:
        g2.add_edge(u, v)
    
    bfs2 = BFSTraversal(g2)
    
    print("Graph structure:")
    print("     A")
    print("    / \\")
    print("   B---C")
    print("   |\\  /|")
    print("   | D  |")
    print("   |/   |")
    print("   E----+")
    print()
    
    print("Basic BFS from 'A':", bfs2.bfs_basic('A'))
    print("Expected:           ['A', 'B', 'C', 'D', 'E'] or ['A', 'B', 'C', 'E', 'D']")
    print()
    
    print("Levels from 'A':", bfs2.bfs_with_levels('A'))
    print("Expected:        [['A'], ['B', 'C'], ['D', 'E']] or [['A'], ['B', 'C'], ['E', 'D']]")
    print()
    
    print("Path A -> E (should find shortest):", bfs2.shortest_path('A', 'E'))
    print("Expected: ['A', 'B', 'E'] (length 3)")
    print()

    # Test Case 3: Disconnected graph
    print("=" * 50)
    print("TEST CASE 3: Disconnected Components")
    print("=" * 50)
    
    g3 = Graph(directed=False)
    # Component 1
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    # Component 2
    g3.add_edge('X', 'Y')
    g3.add_edge('Y', 'Z')
    # Isolated vertex
    g3.add_vertex('M')
    
    bfs3 = BFSTraversal(g3)
    
    print("Graph has 3 components: {A-B-C}, {X-Y-Z}, {M}")
    print()
    
    print("BFS from 'A':", bfs3.bfs_basic('A'))
    print("Expected:     ['A', 'B', 'C']")
    print()
    
    print("BFS from 'M' (isolated):", bfs3.bfs_basic('M'))
    print("Expected:                ['M']")
    print()
    
    print("Path A -> X (disconnected):", bfs3.shortest_path('A', 'X'))
    print("Expected:                    None")
    print()
    
    print("Path A -> A (same vertex):", bfs3.shortest_path('A', 'A'))
    print("Expected:                  ['A']")
    print()

    # Test Case 4: Directed graph
    print("=" * 50)
    print("TEST CASE 4: Directed Graph")
    print("=" * 50)
    
    g4 = Graph(directed=True)
    edges4 = [
        ('A', 'B'), ('B', 'C'),
        ('C', 'D'), ('D', 'B'),  # Cycle: B->C->D->B
        ('A', 'E')
    ]
    for u, v in edges4:
        g4.add_edge(u, v)
    
    bfs4 = BFSTraversal(g4)
    
    print("Directed edges: A->B, B->C, C->D, D->B, A->E")
    print()
    
    print("BFS from 'A':", bfs4.bfs_basic('A'))
    print("Expected:     ['A', 'B', 'E', 'C', 'D']")
    print()
    
    print("BFS from 'D' (can only reach B and C):", bfs4.bfs_basic('D'))
    print("Expected:                               ['D', 'B', 'C']")
    print()
    
    print("Path D -> A (no path in directed graph):", bfs4.shortest_path('D', 'A'))
    print("Expected:                                 None")
    print()

    # Test Case 5: Edge cases
    print("=" * 50)
    print("TEST CASE 5: Edge Cases")
    print("=" * 50)
    
    g5 = Graph(directed=False)
    bfs5 = BFSTraversal(g5)
    
    print("Empty graph - BFS from 'A':", bfs5.bfs_basic('A'))
    print("Expected:                    []")
    print()
    
    g5.add_vertex('A')  # Single vertex
    print("Single vertex - BFS from 'A':", bfs5.bfs_basic('A'))
    print("Expected:                     ['A']")
    print()
    
    print("Single vertex - Levels from 'A':", bfs5.bfs_with_levels('A'))
    print("Expected:                        [['A']]")
    print()
    
    print("Single vertex - Distances from 'A':", bfs5.bfs_shortest_distances('A'))
    print("Expected:                           {'A': 0}")