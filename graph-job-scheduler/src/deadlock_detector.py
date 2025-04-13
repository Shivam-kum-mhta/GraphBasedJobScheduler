class DeadlockDetector:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.rec_stack = set()

    # def detect_deadlock(self):
    #     # Use the graph's method to get all nodes
    #     for node in self.graph.get_nodes():  # Assuming get_nodes() returns a list of all nodes
    #         if node not in self.visited:
    #             if self._is_cyclic(node):
    #                 return True
    #     return False

    def _is_cyclic(self, node):
        self.visited.add(node)
        self.rec_stack.add(node)

        # Access neighbors using the graph's adjacency list
        for neighbor in self.graph.get_neighbors(node):  # Assuming get_neighbors(node) returns neighbors
            if neighbor not in self.visited:
                if self._is_cyclic(neighbor):
                    return True
            elif neighbor in self.rec_stack:
                return True

        self.rec_stack.remove(node)
        return False

    def suggest_fix(self):
        # This method would contain logic to suggest fixes for detected deadlocks.
        # For simplicity, we will return a placeholder message.
        return "Suggested Fix: Remove one of the edges in the cycle."