# main.py

import os
from graph import Graph
from scheduler import Scheduler
from deadlock_detector import DeadlockDetector
from visualizer import Visualizer
from utils.random_dag_generator import create_random_dag

def main():
    input_file = '../data/input.txt'
    num_jobs = 5  # Define the number of jobs to generate
    max_dependencies = 3  # Define a default value for max dependencies

    # Check if input file exists, if not generate a random DAG
    if not os.path.exists(input_file):
        create_random_dag(num_jobs, max_dependencies)

    # Initialize the graph and read job dependencies
    graph = Graph()
    with open(input_file, 'r') as file:
        for line in file:
            # Parse the new input format (e.g., A: [B, C, D])
            line = line.strip()
            if not line:
                continue
            job, dependencies = line.split(':')
            job = job.strip()
            dependencies = dependencies.strip().strip('[]').split(', ')
            graph.add_job(job)
            for dependency in dependencies:
                if dependency:  # Ensure no empty strings are added
                    graph.add_job(dependency)
                    graph.add_dependency(job, dependency)

    print("Graph Adjacency List:", graph.adjacency_list)

    # Initialize the scheduler and detect deadlocks
    scheduler = Scheduler(graph)
    deadlock_detector = DeadlockDetector(graph)
    
    # Check for deadlocks before scheduling
    cycle = deadlock_detector.detect_deadlock()
    if cycle:
        print("Deadlock detected! Cycle found:", " -> ".join(cycle))
        suggested_fix = deadlock_detector.suggest_fix(cycle)
        print(suggested_fix)
        # Don't proceed with scheduling if there's a deadlock
        return
    
    # Perform scheduling
    execution_order = scheduler.topological_sort()
    print("Execution Order:", execution_order)
    # deadlocks = deadlock_detector.detect_deadlock()

    # Output results
    with open('../data/output.txt', 'w') as output_file:
        output_file.write("Job Execution Order: " + " → ".join(execution_order) + "\n")
        # if deadlocks:
        #     output_file.write("Deadlock detected! Cycle found: " + " → ".join(deadlocks) + "\n")
        #     suggested_fix = deadlock_detector.suggest_fix(deadlocks)
        #     output_file.write("Suggested Fix: " + suggested_fix + "\n")
        # else:
        #     output_file.write("No Deadlocks Found.\n")

    # # Visualize the job graph
    # visualizer = Visualizer(graph)
    # visualizer.render_graph(execution_order)

if __name__ == "__main__":
    main()