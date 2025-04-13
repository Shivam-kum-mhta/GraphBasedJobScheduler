import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency list
adjacency_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['I', 'J'],
    'G': [],
    'H': ['J', 'K'],
    'I': [],
    'J': ['K'],
    'K': []
}

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes and edges to the graph
for node, neighbors in adjacency_list.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Generate positions for nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True, edge_color='gray')
plt.title("Graph Representation of the Adjacency List")
plt.show()