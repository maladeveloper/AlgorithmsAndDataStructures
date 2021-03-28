from Graph import MatrixGraph

my_graph = MatrixGraph()

test_edges = [
    ["M", 2, "L"], 
    ["L", 4, "M"],
]

[my_graph.add_edge(edge) for edge in test_edges]
