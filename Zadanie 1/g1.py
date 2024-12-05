import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

# Load .csv files
c1 = pd.read_csv('1c.csv')
crs1 = pd.read_csv('1crs.csv')
ers1 = pd.read_csv('1ers.csv')
c2 = pd.read_csv('2c.csv')
crs2 = pd.read_csv('2crs.csv')

# Calculate average wins
def calculate_avg_wins(data):
    return (data.iloc[:, 2:].mean(axis=1)) * 100

avg_c1 = calculate_avg_wins(c1)
avg_crs1 = calculate_avg_wins(crs1)
avg_ers1 = calculate_avg_wins(ers1)
avg_c2 = calculate_avg_wins(c2)
avg_crs2 = calculate_avg_wins(crs2)

# [Effort] and [generation]
effort = c1['effort'] / 1000 
generation = c1['generation']

# Plotting
fig, xy = plt.subplots(figsize=(7, 6))

# Plot each average wins line
plt.plot(effort, avg_ers1, label='1-Evol-RS', color='blue', marker='o', markevery=25, mec="black")
plt.plot(effort, avg_crs1, label='1-Coev-RS', color='green', marker='v', markevery=25, mec="black")
plt.plot(effort, avg_crs2, label='2-Coev-RS', color='red', marker='D', markevery=25, mec="black")
plt.plot(effort, avg_c1, label='1-Coev', color='black', marker='s', markevery=25, mec="black")
plt.plot(effort, avg_c2, label='2-Coev', color='magenta', marker='D', markevery=25, mec="black")

# Set labels
xy.set_xlabel('Rozegranych gier (x1000)')
xy.set_ylabel('Odsetek wygranych gier [%]')

# Set grid
xy.grid(True, linestyle=(0,(1,5)), color='gray', linewidth=0.8)

# Set x-ticks
xy.set_xticks(np.arange(0, 501, 100))  
xy.set_xlim(0, 500)  

xy.set_yticks(np.arange(60, 101, 5))  
xy.set_ylim(60, 100)

topx = xy.twiny()
topx.set_xticks(np.arange(0, 2000, 40))
topx.set_xlim(0, 200)
topx.set_xlabel('Pokolenie')

# Custom Legend with double markers
legend_elements = [
    Line2D([0], [0], color='blue', lw=1, marker='o', markersize=8, mec="black", label='1-Evol-RS', markerfacecolor='blue'),
    Line2D([0], [0], color='green', lw=1, marker='v', markersize=8, mec="black", label='1-Coev-RS', markerfacecolor='green'),
    Line2D([0], [0], color='red', lw=1, marker='D', markersize=8, mec="black", label='2-Coev-RS', markerfacecolor='red'),
    Line2D([0], [0], color='black', lw=1, marker='s', markersize=8, mec="black", label='1-Coev', markerfacecolor='black'),
    Line2D([0], [0], color='magenta', lw=1, marker='D', markersize=8, mec="black", label='2-Coev', markerfacecolor='magenta')
]

xy.tick_params(axis='x', direction='in')
xy.tick_params(axis='y', direction='in')

# Add legend to plot
xy.legend(handles=legend_elements, loc='upper left')

# Show the plot
plt.show()
