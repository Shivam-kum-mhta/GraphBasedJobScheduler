import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_job(self):
        self.graph.add_job('A')
        self.graph.add_job('B')
        self.assertIn('A', self.graph.adjacency_list)
        self.assertIn('B', self.graph.adjacency_list)

    def test_add_dependency(self):
        self.graph.add_job('A')
        self.graph.add_job('B')
        self.graph.add_dependency('A', 'B')
        self.assertIn('B', self.graph.adjacency_list['A'])

    def test_adjacency_list(self):
        self.graph.add_job('A')
        self.graph.add_job('B')
        self.graph.add_job('C')
        self.graph.add_dependency('A', 'B')
        self.graph.add_dependency('A', 'C')
        expected_output = {
            'A': ['B', 'C'],
            'B': [],
            'C': []
        }
        self.assertEqual(self.graph.get_adjacency_list(), expected_output)

    def test_no_cycles(self):
        self.graph.add_job('A')
        self.graph.add_job('B')
        self.graph.add_dependency('A', 'B')
        self.graph.add_dependency('B', 'C')
        self.graph.add_dependency('C', 'A')  # This creates a cycle
        self.assertTrue(self.graph.has_cycle())

if __name__ == '__main__':
    unittest.main()