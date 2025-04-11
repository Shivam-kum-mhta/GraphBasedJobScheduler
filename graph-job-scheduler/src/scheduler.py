class Scheduler:
    def __init__(self, graph):
        self.graph = graph

    def topological_sort(self):
        in_degree = {u: 0 for u in self.graph.adjacency_list}
        for u in self.graph.adjacency_list:
            for v in self.graph.adjacency_list[u]:
                in_degree[v] += 1

        queue = [u for u in in_degree if in_degree[u] == 0]
        execution_order = []

        while queue:
            u = queue.pop(0)
            execution_order.append(u)

            for v in self.graph.adjacency_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(execution_order) != len(self.graph.adjacency_list):
            return None  # Cycle detected

        return execution_order

    def job_dependency_count(self):
        return {job: len(dependencies) for job, dependencies in self.graph.adjacency_list.items()}