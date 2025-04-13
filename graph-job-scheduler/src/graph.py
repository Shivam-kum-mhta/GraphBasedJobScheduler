class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_job(self, job):
        if job not in self.adjacency_list:
            self.adjacency_list[job] = []

    def add_dependency(self, job_from, job_to):
        if job_from in self.adjacency_list and job_to in self.adjacency_list:
            self.adjacency_list[job_from].append(job_to)

    def get_adjacency_list(self):
        return self.adjacency_list

    def __str__(self):
        return str(self.adjacency_list)