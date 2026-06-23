import sys

class Vertex:
    def __init__(self, value):
        self.value = value 
        self.edges = []
        # vars for BFS 
        self.color = None 
        self.parent = None
        self.distance = sys.maxsize

    # A d:0 [B C E G ]
    def __str__(self):
        parent = "None" if self.parent is None else self.parent.value
        s = self.value + " d:" + str(self.distance) + " p:" + parent + " ["
        for e in self.edges:
            s += e.vertex.value
        s += "]"
        return s
    
    def add_connection(self, vertex, dist=1):
        self.edges.append(Edge(vertex, dist))

    
class Edge:
    def __init__(self, vertex, dist=1):
        self.vertex = vertex 
        self.weight = dist

    
class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        self.vertices.append(Vertex(value))

    def get_vertex(self, value):
        for v in self.vertices:
            if v.value == value:
                return v 
        return None
    
    def connect_many(self, v1, *args):
        for arg in args:
            self.connect(v1, arg)

    def connect(self, v1, v2, dist=1):
        vertex1 = self.get_vertex(v1)
        vertex2 = self.get_vertex(v2)
        if vertex1 is not None and vertex2 is not None:
            vertex1.add_connection(vertex2, dist)
            vertex2.add_connection(vertex1, dist)
        else:
            print("One or both vertices not found")

    def display(self):
        for v in self.vertices:
            print(v)

    def init_vertices(self):
        for vertex in self.vertices:
            vertex.parent = None
            vertex.color = 'white'
            vertex.distance = sys.maxsize

    def bfs(self, starting_value):
        self.init_vertices()
        vertex = self.get_vertex(starting_value)
        if vertex is None:
            print(f"{starting_value} not in the Graph")
        else:
            q = []
            vertex.distance = 0
            vertex.color = 'gray'
            q.append(vertex)
            while len(q) > 0:
                vertex = q.pop(0)
                for connection in vertex.edges:
                    v = connection.vertex
                    if v.color == 'white':
                        v.distance = vertex.distance + 1
                        v.color = 'gray'
                        v.parent = vertex
                        q.append(v)
                vertex.color = 'black'

    def relax(self, u, v, w):
        if v.distance > u.distance + w:
            v.distance = u.distance + w
            v.parent = u

    def print_path(self, start_value, dest_value):
        start = self.get_vertex(start_value)
        dest = self.get_vertex(dest_value) 
        if start is None or dest is None:
            print("One or both vertices not found")
        else:
            self.print_path_recursive(start, dest)
            print()

    def print_path_recursive(self, start, dest):
        if start == dest:
            print(start.value, end=' ')
        elif dest.parent is None:
            print(f"No path to {start.value} from {dest.value}")
        else:
            self.print_path_recursive(start, dest.parent)
            print(dest.value, end=' ')

    def dijkstra(self, start):
        self.init_vertices()
        v = self.get_vertex(start)
        if v is None:
            print(f"Vertex {start} not found")
            return
        v.distance = 0
        Q = []
        for vertex in self.vertices:
            Q.append(vertex)
        while len(Q) > 0:
            # Sort the queue
            Q.sort(key=lambda x : x.distance)
            u = Q.pop(0)
            for e in u.edges:
                v = e.vertex
                w = e.weight
                self.relax(u, v, w)


            



# EXAMPLE FOR BFS
# values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]   

# graph = Graph()
# for value in values:
#     graph.add_vertex(value)

# graph.connect_many("A", "B", "C", "E")
# graph.connect_many("B", "D")
# graph.connect_many("C", "F", "D")
# graph.connect_many("D", "F")
# graph.connect_many("E", "F")
# graph.connect_many("F", "G", "H")
# graph.connect_many("G", "H")
# graph.connect_many("J", "K")

# graph.bfs("A")
# graph.print_path("A", "H")

# graph.display()

# EXAMPLE FOR DIJKSTRA
values = ["A", "B", "C", "D", "E", "F", "G"]
connections = [
    ["A", "B", 4], ["A", "E", 5], ["A", "D", 3], ["B", "C", 2], ["B", "E", 2],
    ["D", "G", 1], ["E", "C", 3], ["E", "F", 6], ["E", "G", 4],
    ["C", "F", 1], ["G", "F", 1]
]

graph = Graph()
for value in values:
    graph.add_vertex(value)

for conn in connections:
    graph.connect(conn[0], conn[1], conn[2])

graph.dijkstra("A")
graph.print_path("A", "C")

graph.display()