
import heapq 

Q = [56, 23, 12, 45, 57, 4, 12]

heapq.heapify(Q)

print(Q)

class Test:
    def __init__(self, name, value):
        self.name = name
        self.value = value 

    def __str__(self):
        return self.name + " " + str(self.value)
    
    def __lt__(self, other):
        return self.value < other.value
 
Q = [Test("A", 12), Test("G", 3), Test("K", 7), Test("B", 1), Test("W", 4)]
heapq.heapify(Q) 

for v in Q:
    print(v)
