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

heapq.heappush(data, Edge("A", "B", 6))
heapq.heappush(data, Edge("A", "C", 3))
heapq.heappush(data, Edge("D", "B", 7))
heapq.heappush(data, Edge("D", "F", 1))
heapq.heappush(data, Edge("K", "B", 2))

top = heapq.heappop(data)

print(top)
print(data[0])