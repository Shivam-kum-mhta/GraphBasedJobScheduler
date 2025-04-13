import unittest
from src.deadlock_detector import DeadlockDetector

class TestDeadlockDetector(unittest.TestCase):

    def setUp(self):
        self.detector = DeadlockDetector()

    def test_no_deadlock(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': ['E'],
            'E': []
        }
        self.detector.load_graph(graph)
        self.assertFalse(self.detector.detect_deadlock())

    def test_deadlock_detected(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        self.detector.load_graph(graph)
        self.assertTrue(self.detector.detect_deadlock())
        cycle = self.detector.get_cycle()
        self.assertEqual(cycle, ['A', 'B', 'C'])

    def test_suggest_fix(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        self.detector.load_graph(graph)
        self.detector.detect_deadlock()
        suggested_fix = self.detector.suggest_fix()
        self.assertIn('Remove edge B → A', suggested_fix)

if __name__ == '__main__':
    unittest.main()