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
            G.add_node(job)
            for dependency in dependencies:
                G.add_edge(dependency, job)

        # Set node colors based on execution order
        color_map = []
        for node in G.nodes():
            if execution_order and node in execution_order:
                color_map.append('green')  # Jobs in execution order
            elif not any(node in dependencies for dependencies in self.graph.adjacency_list.values()):
                color_map.append('red')  # End jobs
            else:
                color_map.append('blue')  # Start jobs

        # Draw the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color_map, arrows=True)
        plt.title("Job Dependency Graph")
        plt.show()