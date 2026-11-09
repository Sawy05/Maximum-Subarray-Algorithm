import heapq
from collections import defaultdict


class DynamicGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)

    # -----------------------------------
    # Graph Operations
    # -----------------------------------

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def delete_edge(self, u, v):
        if v in self.graph[u]:
            del self.graph[u][v]

    def update_weight(self, u, v, w):
        if v in self.graph[u]:
            self.graph[u][v] = w

    # -----------------------------------
    # Initial Dijkstra
    # -----------------------------------

    def dijkstra(self, source):
        self.source = source

        self.dist = {v: float('inf') for v in self.V}
        self.parent = {v: None for v in self.V}

        self.dist[source] = 0

        pq = [(0, source)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > self.dist[u]:
                continue

            for v, w in self.graph[u].items():

                new_dist = self.dist[u] + w

                if new_dist < self.dist[v]:
                    self.dist[v] = new_dist
                    self.parent[v] = u

                    heapq.heappush(pq, (new_dist, v))

    # -----------------------------------
    # Propagation Function
    # Used after improvements
    # -----------------------------------

    def propagate_improvement(self, start):
        pq = [(self.dist[start], start)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > self.dist[u]:
                continue

            for v, w in self.graph[u].items():

                new_dist = self.dist[u] + w

                if new_dist < self.dist[v]:
                    self.dist[v] = new_dist
                    self.parent[v] = u

                    heapq.heappush(pq, (new_dist, v))

    # -----------------------------------
    # Insert Edge
    # -----------------------------------

    def insert_edge(self, u, v, w):

        print(f"\nInsertEdge({u}, {v}, {w})")

        self.graph[u][v] = w

        # Check if new edge improves shortest path
        if self.dist[u] + w < self.dist[v]:

            self.dist[v] = self.dist[u] + w
            self.parent[v] = u

            # propagate improvement
            self.propagate_improvement(v)

    # -----------------------------------
    # Delete Edge
    # -----------------------------------

    def delete_edge_dynamic(self, u, v):

        print(f"\nDeleteEdge({u}, {v})")

        # Check if edge exists
        if v not in self.graph[u]:
            return

        # Was it part of shortest path tree?
        affected = (self.parent[v] == u)

        del self.graph[u][v]

        # If not in shortest path tree -> no effect
        if not affected:
            return

        # Invalidate affected node
        self.dist[v] = float('inf')
        self.parent[v] = None

        # Recompute only affected region
        self.recompute_from(v)

    # -----------------------------------
    # Weight Update
    # -----------------------------------

    def update_weight_dynamic(self, u, v, new_w):

        print(f"\nUpdateWeight({u}, {v}, {new_w})")

        if v not in self.graph[u]:
            return

        old_w = self.graph[u][v]
        self.graph[u][v] = new_w

        # -----------------------------------
        # Weight Decrease
        # -----------------------------------
        if new_w < old_w:

            if self.dist[u] + new_w < self.dist[v]:

                self.dist[v] = self.dist[u] + new_w
                self.parent[v] = u

                self.propagate_improvement(v)

        # -----------------------------------
        # Weight Increase
        # -----------------------------------
        else:

            # Only matters if edge is in shortest path tree
            if self.parent[v] == u:

                self.dist[v] = float('inf')
                self.parent[v] = None

                self.recompute_from(v)

    # -----------------------------------
    # Partial Recompute
    # -----------------------------------

    def recompute_from(self, start):

        pq = []

        # Find alternative incoming edges
        for x in self.V:
            for y, w in self.graph[x].items():

                if y == start:

                    if self.dist[x] + w < self.dist[start]:
                        self.dist[start] = self.dist[x] + w
                        self.parent[start] = x

        heapq.heappush(pq, (self.dist[start], start))

        while pq:

            current_dist, u = heapq.heappop(pq)

            if current_dist > self.dist[u]:
                continue

            for v, w in self.graph[u].items():

                new_dist = self.dist[u] + w

                if new_dist < self.dist[v]:

                    self.dist[v] = new_dist
                    self.parent[v] = u

                    heapq.heappush(pq, (new_dist, v))

    # -----------------------------------
    # Query
    # -----------------------------------

    def query(self, v):

        if self.dist[v] == float('inf'):
            return "INF"

        return self.dist[v]

    # -----------------------------------
    # Display
    # -----------------------------------

    def print_state(self):

        print("\nCurrent Shortest Distances:")

        for v in self.V:
            print(f"dist({v}) = {self.dist[v]}")

        print("\nPredecessor Tree:")

        for v in self.V:
            print(f"{v} <- {self.parent[v]}")


# =====================================================
# Example Usage
# =====================================================

vertices = ['A', 'B', 'C']

g = DynamicGraph(vertices)

# Initial Graph
g.add_edge('A', 'B', 2)
g.add_edge('B', 'C', 3)
g.add_edge('A', 'C', 5)

# Run Initial Dijkstra
print("Initial Dijkstra from A")

g.dijkstra('A')

g.print_state()

# =====================================================
# Update 1
# InsertEdge(B, C, 1)
# =====================================================

g.insert_edge('B', 'C', 1)

g.print_state()

# =====================================================
# Update 2
# DeleteEdge(A, C)
# =====================================================

g.delete_edge_dynamic('A', 'C')

g.print_state()

# =====================================================
# Update 3
# UpdateWeight(B, C, 10)
# =====================================================

g.update_weight_dynamic('B', 'C', 10)

g.print_state()

# =====================================================
# Query Example
# =====================================================

print("\nQuery(C) =", g.query('C'))