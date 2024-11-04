import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_points = 10000

#square
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")           
ax.set_xlim(-1, 1)              
ax.set_ylim(-1, 1)               
ax.set_title("Estimating Pi using Monte Carlo Simulation")
ax.add_patch(plt.Circle((0, 0), 1, color='black', fill=False))  


inside_x, inside_y = [], []
outside_x, outside_y = [], []

inside_scatter = ax.scatter([], [], color="blue", s=5, label="Inside Circle")
outside_scatter = ax.scatter([], [], color="red", s=5, label="Outside Circle")



def update(i):
    
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)
    
    inside_scatter.set_offsets(np.c_[inside_x, inside_y])
    outside_scatter.set_offsets(np.c_[outside_x, outside_y])
    
    # Calculate Pi
    pi_estimate = 4 * len(inside_x) / (len(inside_x) + len(outside_x))
    
    # Update 
    ax.set_title(f"Estimating Pi using Monte Carlo Simulation- 190132\nEstimated Pi = {pi_estimate:.5f}")


ani = FuncAnimation(fig, update, frames=num_points, interval=1, repeat=False)
plt.show()
