import unittest
from src.scheduler import Scheduler
from src.graph import Graph

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()
        self.graph = Graph()
        self.graph.add_job('A')
        self.graph.add_job('B')
        self.graph.add_job('C')
        self.graph.add_job('D')
        self.graph.add_job('E')
        self.graph.add_dependency('A', 'B')
        self.graph.add_dependency('A', 'C')
        self.graph.add_dependency('B', 'D')
        self.graph.add_dependency('C', 'D')
        self.graph.add_dependency('D', 'E')
        self.scheduler.set_graph(self.graph)

    def test_topological_sort(self):
        execution_order = self.scheduler.topological_sort()
        self.assertEqual(execution_order, ['A', 'B', 'C', 'D', 'E'])

    def test_dependency_count(self):
        dependency_count = self.scheduler.get_dependency_count()
        expected_count = {'A': 2, 'B': 1, 'C': 1, 'D': 1, 'E': 0}
        self.assertEqual(dependency_count, expected_count)

    def test_deadlock_detection_no_deadlock(self):
        self.assertFalse(self.scheduler.detect_deadlock())

    def test_deadlock_detection_with_deadlock(self):
        self.graph.add_dependency('E', 'A')  # Introduce a cycle
        self.scheduler.set_graph(self.graph)
        self.assertTrue(self.scheduler.detect_deadlock())

if __name__ == '__main__':
    unittest.main()