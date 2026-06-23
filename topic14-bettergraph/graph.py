import sys
import heapq

class VertexUtils:
    def __init__(self):
        self.color = None 
        self.parent = None
        self.distance = sys.maxsize


class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest 
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
    
    def __str__(self):
        return self.source.key + " " + self.dest.key + " " \
            + str(self.weight)


class Vertex:
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.edges = []
        self.utils = VertexUtils()

    def add_connection(self, dest, distance):
        e = Edge(self, dest, distance)
        self.edges.append(e)

    def __str__(self):
        s = str(self.key) + " ["
        for e in self.edges:
            s += e.dest.key + ":" + str(e.weight) + " "
        s += ']'
        return str(s)


class Graph:
    def __init__(self):
        self.directed = False
        self.weighted = False 
        self.vertices = {}

    def add_vertex(self, key, value=None):
        if key in self.vertices:
            print(f"{key} already in graph.")
        else:
            vertex = Vertex(key, value)
            self.vertices[key] = vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def display(self):
        for key in self.vertices:
            print(self.vertices[key])

    def connect(self, v1, v2, dist=1):
        vertex1 = self.get_vertex(v1)
        vertex2 = self.get_vertex(v2)
        if vertex1 is not None and vertex2 is not None:
            vertex1.add_connection(vertex2, dist)
            if not self.directed:
                vertex2.add_connection(vertex1, dist)
        else:
            print("One or both vertices not found")

    def connect_many(self, vertex_edge_list):
        for value in vertex_edge_list:
            self.connect(value[0], value[1], value[2])

    def min_spanning_tree(self, starting):
        visited_vertices = []
        selected_edges = [] 
        edges_to_select = []
        current = self.get_vertex(starting)
        while len(visited_vertices) < len(self.vertices):
            visited_vertices.append(current.key)

            for edge in current.edges:
                if edge.dest.key not in visited_vertices:
                    heapq.heappush(edges_to_select, edge)
            
            # Remove edges on top where destination is visited
            while len(edges_to_select) > 0 and edges_to_select[0].dest.key in visited_vertices:
                heapq.heappop(edges_to_select)
      
            # Get next edge and go to its destination vertex
            if len(edges_to_select) > 0:
                selected_edges.append(edges_to_select[0])
                current = edges_to_select[0].dest
                heapq.heappop(edges_to_select)
            
        # PRINT
        print(visited_vertices)
        for edge in selected_edges:
            print(edge)

    def hamiltonian_cycle(self, starting):
        start_vertex = self.get_vertex(starting)
        if start_vertex is None:
            print(f"Vertex {starting} not found")
            return None 

        path = [starting]
        visited = {starting}

        def backtrack():
            # BASE CASE
            if len(path) == len(self.vertices):  # we have all vertices into the path
                current = self.get_vertex(path[-1])
                for edge in current.edges:
                    if edge.dest.key == starting:
                        return True
                return False
            
            current = self.get_vertex(path[-1])
            for edge in current.edges:
                key = edge.dest.key
                if key not in visited:
                    path.append(key)
                    visited.add(key)

                    if backtrack():
                        return True 
                    
                    path.pop()
                    visited.remove(key)
            return False

        
        if backtrack():
            hamiltonian = path + [starting]
            print("Hamiltonican cycle found")
            return hamiltonian
        else:
            print("No Hamiltonian cycle found")
            return None



