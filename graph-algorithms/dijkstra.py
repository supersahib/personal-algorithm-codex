"""
Algorithm: Dijkstra's Shortest Path
Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V)
Category: Graph Algorithms - Shortest Path

Description:
    Finds shortest paths from source to all vertices in weighted graph
    Greedy approach: always process closest unvisited vertex
    Only works with non-negative edge weights

Use Cases:
    - GPS navigation systems
    - Network routing protocols
    - Flight connections
    - Game pathfinding (with uniform costs)

LeetCode Problems:
    - #743: Network Delay Time
    - #787: Cheapest Flights Within K Stops
    - #1514: Path with Maximum Probability
"""

import heapq
from typing import Dict, List, Optional, Tuple
INF = float('inf')

class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = {} #neighbor_vertex -->weight
    
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
    def __init__(self, directed = False):
        self.vertices = {} # key -> Vertex object
        self.num_vertices = 0
        self.directed = directed
    
    def add_vertex(self, key):
        if key in self.vertices:
            return None
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        self.num_vertices += 1
        return new_vertex
    
    def add_edge(self, from_key, to_key, weight=1):
        if from_key not in self.vertices:
            self.add_vertex(from_key)
        if to_key not in self.vertices:
            self.add_vertex(to_key)
        
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)
        # if undirected, add edge from to-->from
        if not self.directed:
            self.vertices[to_key].add_neighbor(self.vertices[from_key], weight)
    
    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        """make graph iterable over vertices"""
        return iter(self.vertices.values())



class DijkstraTraversal:
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def dijkstra_distances(self, start_key) -> Dict[str, float]:
        """
        Find shortest distances from start to all reachable vertices
        
        Returns:
            Dictionary mapping vertex_key -> shortest_distance
        """
        if start_key not in self.graph.vertices:
            return {}
        
        # Initialize distances
        distances = {vertex: INF for vertex in self.graph.vertices}
        distances[start_key] = 0
        
        # Priority queue: (distance, vertex_key)
        pq = [(0, start_key)]
        visited = set()
        
        while pq:
            current_dist, current_key = heapq.heappop(pq)
            
            # Skip if already visited 
            if current_key in visited:
                continue
            current_vertex = self.graph.vertices[current_key]
            
            #mark as viisted as we are processing it
            visited.add(current_key)

            # Process each neighbor
            # Remember: neighbors dict has vertex -> weight
            for neighbor_vertex, edge_weight in current_vertex.neighbors.items():
                if neighbor_vertex.id in visited:
                    continue
                #Relax (u,v,w)
                new_dist = current_dist + edge_weight
                if new_dist < distances[neighbor_vertex.id]:
                    distances[neighbor_vertex.id] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor_vertex.id))
        return distances
    
    def shortest_path(self, start_key, end_key) -> Optional[Tuple[List, float]]:
        """
        Find shortest path and its cost between two vertices
        
        Returns:
            Tuple of (path_list, total_cost) or None if no path
        """
        if start_key not in self.graph.vertices or end_key not in self.graph.vertices:
            return None
            
        distances = {vertex: INF for vertex in self.graph.vertices}
        distances[start_key] = 0
        parent = {start_key: None}
        
        pq = [(0, start_key)]
        visited = set()
        
        while pq:
            current_dist, current_key = heapq.heappop(pq)
            
            if current_key == end_key:
                # Reconstruct path using parent pointers
                path = []
                current = end_key
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return (path, distances[end_key])

            if current_key in visited:
                continue
            
            visited.add(current_key)
            current_vertex = self.graph.vertices[current_key]
            
            for neighbor_vertex, edge_weight in current_vertex.neighbors.items():
                if neighbor_vertex.id in visited:
                    continue
                #Relax (u,v,w)
                new_dist = current_dist + edge_weight
                if new_dist < distances[neighbor_vertex.id]:
                    distances[neighbor_vertex.id] = new_dist
                    parent[neighbor_vertex.id] = current_key
                    heapq.heappush(pq, (new_dist, neighbor_vertex.id))
            
        if distances[end_key] == INF:
            return None


if __name__ == "__main__":
    print("=" * 60)
    print("TEST CASE 1: Basic Weighted Graph")
    print("=" * 60)
    
    g1 = Graph(directed=False)
    
    # Create a simple weighted graph
    #     4     3
    #  A --- B --- D
    #  |     |     |
    # 2|    1|     |2
    #  |     |     |
    #  C --- --- - E
    #      10
    
    weighted_edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 3),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for u, v, w in weighted_edges:
        g1.add_edge(u, v, w)
    
    dijkstra1 = DijkstraTraversal(g1)
    
    print("Graph edges:", weighted_edges)
    print()
    
    # Test dijkstra_distances
    distances = dijkstra1.dijkstra_distances('A')
    print("Distances from 'A':", distances)
    print("Expected: {'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 8}")
    print("Note: A->C->B (2+1=3) is shorter than direct A->B (4)")
    print()
    
    # Test shortest_path
    path, cost = dijkstra1.shortest_path('A', 'E')
    print(f"Shortest path A->E: {path}, Cost: {cost}")
    print("Expected: ['A', 'C', 'B', 'D', 'E'], Cost: 8")
    print()
    
    # Test different starting point
    distances_from_d = dijkstra1.dijkstra_distances('D')
    print("Distances from 'D':", distances_from_d)
    print("Expected: {'A': 6, 'B': 3, 'C': 4, 'D': 0, 'E': 2}")
    print()

    print("=" * 60)
    print("TEST CASE 2: Directed Graph")
    print("=" * 60)
    
    g2 = Graph(directed=True)
    
    # Directed graph where some paths don't exist
    directed_edges = [
        ('A', 'B', 5),
        ('B', 'C', 3),
        ('C', 'D', 2),
        ('A', 'D', 15),  # Direct but expensive
        ('D', 'E', 1),
        ('B', 'E', 10)   # Alternative path to E
    ]
    
    for u, v, w in directed_edges:
        g2.add_edge(u, v, w)
    
    dijkstra2 = DijkstraTraversal(g2)
    
    print("Directed edges:", directed_edges)
    print()
    
    path, cost = dijkstra2.shortest_path('A', 'E')
    print(f"Shortest path A->E: {path}, Cost: {cost}")
    print("Expected: ['A', 'B', 'C', 'D', 'E'], Cost: 11")
    print("(A->D->E would be 16, A->B->E would be 15)")
    print()
    
    # Test unreachable node (no path from E to A in directed graph)
    result = dijkstra2.shortest_path('E', 'A')
    print(f"Path E->A in directed graph: {result}")
    print("Expected: None (no path exists)")
    print()

    print("=" * 60)
    print("TEST CASE 3: Graph with Multiple Equal Shortest Paths")
    print("=" * 60)
    
    g3 = Graph(directed=False)
    
    # Diamond shape with equal paths
    equal_edges = [
        ('S', 'A', 5),
        ('S', 'B', 5),
        ('A', 'T', 5),
        ('B', 'T', 5),
        ('A', 'B', 1)  # Cross edge
    ]
    
    for u, v, w in equal_edges:
        g3.add_edge(u, v, w)
    
    dijkstra3 = DijkstraTraversal(g3)
    
    distances = dijkstra3.dijkstra_distances('S')
    print("Graph with equal paths - distances from 'S':", distances)
    print("Expected: {'S': 0, 'A': 5, 'B': 5, 'T': 10}")
    print()
    
    path, cost = dijkstra3.shortest_path('S', 'T')
    print(f"One shortest path S->T: {path}, Cost: {cost}")
    print("Could be ['S', 'A', 'T'] or ['S', 'B', 'T'], both cost 10")
    print()

    print("=" * 60)
    print("TEST CASE 4: Disconnected Graph")
    print("=" * 60)
    
    g4 = Graph(directed=False)
    
    # Two separate components
    g4.add_edge('A', 'B', 3)
    g4.add_edge('B', 'C', 4)
    
    g4.add_edge('X', 'Y', 5)
    g4.add_edge('Y', 'Z', 6)
    
    dijkstra4 = DijkstraTraversal(g4)
    
    distances = dijkstra4.dijkstra_distances('A')
    print("Distances from 'A' (can't reach X,Y,Z):")
    print(distances)
    print("Expected: A=0, B=3, C=7, X=inf, Y=inf, Z=inf")
    print()
    
    result = dijkstra4.shortest_path('A', 'X')
    print(f"Path A->X (disconnected): {result}")
    print("Expected: None")
    print()

    print("=" * 60)
    print("TEST CASE 5: Single Node and Edge Cases")
    print("=" * 60)
    
    g5 = Graph(directed=False)
    g5.add_vertex('A')
    
    dijkstra5 = DijkstraTraversal(g5)
    
    distances = dijkstra5.dijkstra_distances('A')
    print("Single node distances:", distances)
    print("Expected: {'A': 0}")
    print()
    
    # Test same start and end
    path, cost = dijkstra5.shortest_path('A', 'A')
    print(f"Path A->A: {path}, Cost: {cost}")
    print("Expected: ['A'], Cost: 0")