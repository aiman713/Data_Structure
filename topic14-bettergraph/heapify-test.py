import heapq 


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
    
    def __str__(self):
        return self.v1 + " " + self.v2 + " " + str(self.weight)
    

data = []
heapq.heapify(data)

# Error appending and pop from a heap, instead of
# heappush and heappop
data.append(Edge("A", "B", 6))
data.append(Edge("A", "C", 3))
data.append(Edge("D", "B", 7))
data.append(Edge("D", "F", 1))
data.append(Edge("K", "B", 2))


top = data.pop(0)
print(top)

print(data[0])