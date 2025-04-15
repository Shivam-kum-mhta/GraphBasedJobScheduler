class Visualizer:
    def __init__(self, graph):
        self.graph = graph

    def render_graph(self, execution_order=None):
        import matplotlib
        matplotlib.use('TkAgg')  # Use an interactive backend
        import matplotlib.pyplot as plt
        import networkx as nx
        from matplotlib.animation import FuncAnimation
        from matplotlib.text import Text

        G = nx.DiGraph()

        # Add nodes and edges to the graph
        for job, dependencies in self.graph.adjacency_list.items():
            G.add_node(job)
            for dependency in dependencies:
                G.add_edge(job, dependency)

        # Set up the figure
        fig, ax = plt.subplots(figsize=(12, 10))
        pos = nx.spring_layout(G)

        def update(frame):
            ax.clear()
            # Color nodes based on execution progress
            color_map = []
            for node in G.nodes():
                if node in execution_order[:frame+1]:
                    color_map.append('green')  # Completed jobs
                elif node == execution_order[frame] if frame < len(execution_order) else None:
                    color_map.append('yellow')  # Current job
                else:
                    color_map.append('blue')  # Pending jobs

            # Draw the graph
            nx.draw(G, pos, with_labels=True, node_color=color_map, 
                   arrows=True, edge_color='gray', ax=ax)
            
            # Create the title with step information
            step_text = f"Step {frame+1}: Executing Job {execution_order[frame]}" if frame < len(execution_order) else "Job Execution Complete"
            ax.set_title(step_text, pad=20, fontsize=12, color='black')

            # Create horizontal execution order text
            exec_text = "Execution Order: "
            x_pos = 0.1  # Starting x-position for the text
            y_pos = 0.95  # Fixed y-position for the text
            
            # Add the label
            ax.text(x_pos, y_pos, exec_text, color='black', 
                   ha='left', transform=ax.transAxes, fontsize=10)
            x_pos += 0.15  # Move right after the label

            # Add each job and arrow
            for i, job in enumerate(execution_order):
                if i < frame:
                    color = 'green'  # Completed jobs
                elif i == frame:
                    color = 'orange'  # Current job
                else:
                    color = 'black'  # Pending jobs
                
                # Add the job
                ax.text(x_pos, y_pos, job, color=color, 
                       ha='center', transform=ax.transAxes, fontsize=10)
                x_pos += 0.03  # Reduced spacing for the job
                
                # Add arrow if not the last job
                if i < len(execution_order) - 1:
                    ax.text(x_pos, y_pos, "→", color='black',
                           ha='center', transform=ax.transAxes, fontsize=10)
                    x_pos += 0.02  # Reduced spacing for the arrow

            # Add legend
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor='green', label='Completed Jobs'),
                Patch(facecolor='yellow', label='Current Job'),
                Patch(facecolor='blue', label='Pending Jobs')
            ]
            ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))

        # Create animation
        if execution_order:
            anim = FuncAnimation(fig, update, frames=len(execution_order)+1, 
                               interval=1000, repeat=False)
            plt.tight_layout()
            plt.show()
        else:
            # If no execution order, just show the static graph
            color_map = ['blue' for _ in G.nodes()]
            nx.draw(G, pos, with_labels=True, node_color=color_map, 
                   arrows=True, edge_color='gray', ax=ax)
            ax.set_title("Job Dependency Graph", pad=20, fontsize=12)
            
            # Add legend for static graph
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor='blue', label='Jobs')
            ]
            ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))
            
            plt.tight_layout()
            plt.show()