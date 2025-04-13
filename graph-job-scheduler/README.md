# Graph-Based Job Scheduling System

## Introduction
The Graph-Based Job Scheduling System is designed to efficiently manage job scheduling based on their dependencies using a Directed Acyclic Graph (DAG). This project implements various graph algorithms to determine the execution order of jobs, detect deadlocks, and visualize the scheduling process.

## Features
- **Job Scheduling**: Organizes jobs based on their dependencies.
- **Deadlock Detection**: Identifies cycles in the job graph to prevent deadlocks.
- **Visualization**: Provides a graphical representation of job dependencies and execution order.
- **Random DAG Generation**: Generates random job dependencies for testing purposes.

## Project Structure
```
graph-job-scheduler
├── src
│   ├── main.py               # Entry point for the application
│   ├── graph.py              # Graph class for job dependencies
│   ├── scheduler.py          # Scheduler class for job scheduling
│   ├── deadlock_detector.py   # Deadlock detection class
│   ├── visualizer.py         # Visualization class for job graph
│   └── utils
│       └── random_dag_generator.py # Utility for generating random DAGs
├── data
│   ├── input.txt            # Input file for job dependencies
│   └── output.txt           # Output file for scheduling results
├── tests
│   ├── test_graph.py        # Unit tests for Graph class
│   ├── test_scheduler.py     # Unit tests for Scheduler class
│   ├── test_deadlock_detector.py # Unit tests for DeadlockDetector class
│   └── test_visualizer.py    # Unit tests for Visualizer class
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in version control
```

## Installation
1. Clone the repository:

2. Navigate to the project directory:
   ```
   cd graph-job-scheduler
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Prepare the `input.txt` file in the `data` directory with job dependencies in adjacency list format.
2. Run the application:
   ```
   python src/main.py
   ```
3. Check the `output.txt` file in the `data` directory for the scheduling results and any detected deadlocks.

## Future Enhancements
- Implement critical path analysis to find the longest execution time.
- Simulate parallel execution of jobs.
- Add Gantt chart representation for visualizing job scheduling timelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
