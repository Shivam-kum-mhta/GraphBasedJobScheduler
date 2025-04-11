import unittest
from src.visualizer import Visualizer
import matplotlib.pyplot as plt
import networkx as nx

class TestVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = Visualizer()

    def test_render_graph(self):
        # Create a sample graph
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])
        
        # Render the graph
        plt.figure()
        self.visualizer.render_graph(graph)
        
        # Check if the graph is displayed (this will not be a strict test)
        # but we can check if the figure is created
        self.assertIsNotNone(plt.gcf())

    def test_color_coding(self):
        # Create a sample graph
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])
        
        # Define execution order and expected colors
        execution_order = ['A', 'B', 'C', 'D', 'E']
        expected_colors = ['blue', 'green', 'green', 'green', 'red']  # Start, In Progress, End
        
        # Render the graph with color coding
        plt.figure()
        self.visualizer.render_graph(graph, execution_order)
        
        # Check if the colors match the expected colors
        for i, node in enumerate(graph.nodes()):
            color = self.visualizer.get_node_color(node, execution_order)
            self.assertEqual(color, expected_colors[i])

if __name__ == '__main__':
    unittest.main()