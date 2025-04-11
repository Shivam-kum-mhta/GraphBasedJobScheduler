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
            jobs = line.strip().split()
            if len(jobs) == 2:
                graph.add_dependency(jobs[0], jobs[1])

    print("Graph Adjacency List:", graph.adjacency_list)

    # Initialize the scheduler and detect deadlocks
    scheduler = Scheduler(graph)
    deadlock_detector = DeadlockDetector(graph)

    # Perform scheduling
    execution_order = scheduler.topological_sort()
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

    # Visualize the job graph
    visualizer = Visualizer(graph)
    visualizer.render_graph(execution_order)

if __name__ == "__main__":
    main()