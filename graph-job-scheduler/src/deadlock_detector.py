class DeadlockDetector:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.rec_stack = set()
        self.cycle = []

    def detect_deadlock(self):
        """
        Detects if there are any cycles in the job dependency graph.
        Returns the cycle if found, None otherwise.
        """
        self.visited = set()
        self.rec_stack = set()
        self.cycle = []

        # Check each node in the graph
        for node in self.graph.adjacency_list.keys():
            if node not in self.visited:
                if self._is_cyclic(node):
                    return self.cycle
        return None

    def _is_cyclic(self, node):
        """
        Helper method to detect cycles using DFS.
        Returns True if a cycle is found, False otherwise.
        """
        self.visited.add(node)
        self.rec_stack.add(node)
        self.cycle.append(node)

        # Check all neighbors of the current node
        for neighbor in self.graph.adjacency_list.get(node, []):
            if neighbor not in self.visited:
                if self._is_cyclic(neighbor):
                    return True
            elif neighbor in self.rec_stack:
                # Found a cycle
                self.cycle.append(neighbor)
                return True

        self.rec_stack.remove(node)
        self.cycle.pop()
        return False

    def suggest_fix(self, cycle):
        """
        Suggests a fix for the detected deadlock by identifying the edge to remove.
        """
        if not cycle:
            return "No deadlock detected."

        # Find the edge that would break the cycle with minimal impact
        # We'll suggest removing the last edge in the cycle
        if len(cycle) >= 2:
            last_node = cycle[-1]
            first_node = cycle[0]
            return f"Suggested Fix: Remove dependency {last_node} -> {first_node}"
        return "Suggested Fix: Remove one of the self-dependencies"