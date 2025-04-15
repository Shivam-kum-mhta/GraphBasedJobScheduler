# main.py

import os
from graph import Graph
from scheduler import Scheduler
from deadlock_detector import DeadlockDetector
from visualizer import Visualizer
import random
import string

def create_random_adjacency_list(num_jobs):
    """Create a random adjacency list for jobs."""
    # Generate job names (A, B, C, ...)
    jobs = list(string.ascii_uppercase[:num_jobs])
    adjacency_list = {}
    
    for job in jobs:
        # Randomly decide how many dependencies this job will have (0 to 3)
        num_dependencies = random.randint(0, min(3, len(jobs)-1))
        
        # Randomly select dependencies from jobs that come after this job in the alphabet
        # This helps prevent cycles in the graph
        possible_dependencies = [j for j in jobs if j > job]
        dependencies = random.sample(possible_dependencies, min(num_dependencies, len(possible_dependencies)))
        
        adjacency_list[job] = dependencies
    
    return adjacency_list

def write_adjacency_list_to_file(adjacency_list, filename):
    """Write the adjacency list to a file in the required format."""
    with open(filename, 'w') as file:
        for job, dependencies in adjacency_list.items():
            file.write(f"{job}: [{', '.join(dependencies)}]\n")

def main():
    input_file = '../data/input.txt'
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print("Input file not found. Creating a new one with random job dependencies.")
        
        # Get number of jobs from user
        while True:
            try:
                num_jobs = int(input("Enter the number of jobs (between 3 and 26): "))
                if 3 <= num_jobs <= 26:
                    break
                print("Please enter a number between 3 and 26.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Create random adjacency list
        adjacency_list = create_random_adjacency_list(num_jobs)
        
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(input_file), exist_ok=True)
        
        # Write to file
        write_adjacency_list_to_file(adjacency_list, input_file)
        print(f"Created new input file with {num_jobs} jobs.")
        print("You can find the job dependencies in", input_file)

    # Initialize the graph and read job dependencies
    graph = Graph()
    with open(input_file, 'r') as file:
        for line in file:
            # Parse the input format (e.g., A: [B, C, D])
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

    # Output results
    with open('../data/output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("Job Execution Order: " + " → ".join(execution_order) + "\n")

    # Visualize the job graph
    visualizer = Visualizer(graph)
    visualizer.render_graph(execution_order)

if __name__ == "__main__":
    main()