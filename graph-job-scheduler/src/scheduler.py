from collections import deque

class Scheduler:
    def __init__(self, graph):
        self.graph = graph

    def topological_sort(self):
        # Calculate the outdegree for each job
        outdegree = {job: len(dependencies) for job, dependencies in self.graph.adjacency_list.items()}

        # Use a queue to process jobs, starting with those having the smallest outdegree
        queue = deque(sorted(outdegree.keys(), key=lambda job: (outdegree[job], job)))  # Sort by outdegree, then alphabetically
        execution_order = []

        while queue:
            # Process the job with the smallest outdegree
            current_job = queue.popleft()
            execution_order.append(current_job)

            # Remove the current job from the graph and update outdegree of its neighbors
            for neighbor in self.graph.adjacency_list[current_job]:
                outdegree[neighbor] -= 1

            # Re-sort the queue based on updated outdegree and alphabetical order
            queue = deque(sorted(
                [job for job in outdegree if job not in execution_order],
                key=lambda job: (outdegree[job], job)
            ))

        # Check for cycles (if all jobs are not processed)
        if len(execution_order) != len(self.graph.adjacency_list):
            return None  # Cycle detected

        return execution_order

    def job_dependency_count(self):
        return {job: len(dependencies) for job, dependencies in self.graph.adjacency_list.items()}