from graph import Graph

vertices_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
# ["C", "G", 6], 
vertices_edges = [
    ["A", "B", 4], ["A", "D", 6], ["B", "C", 3], ["B", "F", 4],
    ["D", "E", 7], ["D", "H", 2], ["E", "F", 5], ["F", "C", 2],
    ["E", "H", 4], ["F", "G", 3], ["G", "H", 2]
]

gr = Graph()
for v in vertices_list:
    gr.add_vertex(v)
gr.connect_many(vertices_edges)

gr.display()

print("MIN SPANNING TREE")
gr.min_spanning_tree("A")

print("HAMILTONIAN CYCLE")
result = gr.hamiltonian_cycle("A")
if result is None:
    print("No hamiltonian cycle")
else:
    print(result)



                 