from collections import deque, defaultdict

class Scheduler:
    def __init__(self, graph):
        self.graph = graph

    def topological_sort(self):
        # Step 1: Reverse the graph and calculate outdegrees
        reverse_graph = defaultdict(list)
        outdegree = {job: 0 for job in self.graph.adjacency_list}

        # Build the reverse graph and calculate outdegrees
        for job, dependencies in self.graph.adjacency_list.items():
            outdegree[job] = len(dependencies)
            for dependency in dependencies:
                reverse_graph[dependency].append(job)

        # Step 2: Find sink nodes (outdegree == 0)
        queue = deque([job for job, degree in outdegree.items() if degree == 0])

        # Step 3: Perform topological sort using reverse edges
        reverse_topo = []
        while queue:
            current_job = queue.popleft()
            reverse_topo.append(current_job)

            for parent in reverse_graph[current_job]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    queue.append(parent)

        # Step 4: Reverse the result to get the actual topological order
        reverse_topo.reverse()

        # Step 5: Check for cycles
        if len(reverse_topo) != len(self.graph.adjacency_list):
            return None  # Cycle detected

        return reverse_topo

    def job_dependency_count(self):
        return {job: len(dependencies) for job, dependencies in self.graph.adjacency_list.items()}