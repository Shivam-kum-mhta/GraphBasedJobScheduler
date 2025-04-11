import random

def generate_random_dag(num_jobs, max_dependencies):
    graph = {f'Job_{i}': [] for i in range(num_jobs)}
    
    for job in graph:
        num_edges = random.randint(0, max_dependencies)
        dependencies = random.sample([j for j in graph if j != job], num_edges)
        graph[job].extend(dependencies)
    
    return graph

def save_dag_to_file(dag, filename='../data/input.txt'):
    with open(filename, 'w') as f:
        for job, dependencies in dag.items():
            for dep in dependencies:
                f.write(f"{job} {dep}\n")

def create_random_dag(num_jobs=5, max_dependencies=2):
    dag = generate_random_dag(num_jobs, max_dependencies)
    save_dag_to_file(dag)