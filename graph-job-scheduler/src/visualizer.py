class Visualizer:
    def __init__(self, graph):
        self.graph = graph

    def render_graph(self, execution_order=None):
        import matplotlib
        matplotlib.use('TkAgg')  # Use an interactive backend
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.DiGraph()

        # Add nodes and edges to the graph
        for job, dependencies in self.graph.adjacency_list.items():  # Access adjacency_list
            G.add_node(job)  # Add the job as a node
            for dependency in dependencies:
                G.add_edge(job, dependency)  # Add an edge from the job to its dependency (out-degree)

        # Set node colors based on execution order
        color_map = []
        for node in G.nodes():
            if execution_order and node in execution_order:
                color_map.append('green')  # Jobs in execution order
            elif len(list(G.successors(node))) == 0:
                color_map.append('red')  # End jobs (no outgoing edges)
            else:
                color_map.append('blue')  # Start jobs or intermediate jobs

        # Generate positions for nodes in the graph layout
        pos = nx.spring_layout(G)

        # Draw the graph with labels, colors, and arrows for dependencies
        nx.draw(G, pos, with_labels=True, node_color=color_map, arrows=True, edge_color='gray')
        plt.title("Job Dependency Graph (Reversed Execution Order)")
        plt.show()