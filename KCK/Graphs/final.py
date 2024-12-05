import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

c1 = pd.read_csv('1c.csv')
crs1 = pd.read_csv('1crs.csv')
ers1 = pd.read_csv('1ers.csv')
c2 = pd.read_csv('2c.csv')
crs2 = pd.read_csv('2crs.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

font = {
    'family': 'Times New Roman',
    'color':  'black',
    'weight': 'normal',
    'size': 14,
}

#========================================================
# First subplot (Line Plot)
#========================================================

def calculate_avg_wins(data):
    return (data.iloc[:, 2:].mean(axis=1)) * 100

avg_c1 = calculate_avg_wins(c1)
avg_crs1 = calculate_avg_wins(crs1)
avg_ers1 = calculate_avg_wins(ers1)
avg_c2 = calculate_avg_wins(c2)
avg_crs2 = calculate_avg_wins(crs2)

effort = c1['effort'] / 1000 

ax1.plot(effort, avg_ers1, label='1-Evol-RS', color='blue', marker='o', markevery=25, mec="black")
ax1.plot(effort, avg_crs1, label='1-Coev-RS', color='green', marker='v', markevery=25, mec="black")
ax1.plot(effort, avg_crs2, label='2-Coev-RS', color='red', marker='D', markevery=25, mec="black")
ax1.plot(effort, avg_c1, label='1-Coev', color='black', marker='s', markevery=25, mec="black")
ax1.plot(effort, avg_c2, label='2-Coev', color='magenta', marker='D', markevery=25, mec="black")

ax1.set_xticks(np.arange(0, 501, 100))  
ax1.set_xlim(0, 500)  

ax1.set_yticks(np.arange(60, 101, 5), )  
ax1.set_ylim(60, 100)

topx = ax1.twiny()
topx.set_xticks(np.arange(0, 201, 40))
topx.set_xlim(0, 200)

ax1.set_xlabel('Rozegranych gier (x1000)', fontdict = font)
ax1.set_ylabel('Odsetek wygranych gier [%]', fontdict = font)
topx.set_xlabel('Pokolenie', fontdict = font)

ax1.set_xticklabels(ax1.get_xticks(), fontsize = 12, fontname='Times New Roman')
ax1.set_yticklabels(ax1.get_yticks(), fontsize = 12, fontname='Times New Roman')
topx.set_xticklabels(topx.get_xticks(), fontsize = 12, fontname='Times New Roman')

ax1.grid(True, linestyle=(0, (1, 5)), color='gray', linewidth=0.8)

ax1.tick_params(axis='x', direction='in')
topx.tick_params(axis='x', direction='in')
ax1.tick_params(axis='y', direction='in')

ax1.legend(fancybox=True, framealpha = 0.3, numpoints = 2)


#========================================================
# Second subplot (Box Plot)
#========================================================

def last_row_results(data):
    return data.iloc[-1, 2:].dropna()

data_c1 = last_row_results(c1)
data_crs1 = last_row_results(crs1)
data_ers1 = last_row_results(ers1)
data_c2 = last_row_results(c2)
data_crs2 = last_row_results(crs2)

data_to_plot = [data_ers1, data_crs1, data_crs2, data_c1, data_c2]

box = ax2.boxplot(
    data_to_plot, patch_artist=True, notch=True, showmeans=True, meanline=False, widths=0.35,
    boxprops=dict(color='blue', facecolor='none'),
    medianprops=dict(color='red'),
    meanprops=dict(marker='o', markerfacecolor='blue', markeredgecolor='black'),
    whiskerprops=dict(color='blue', linestyle=(0, (10, 3)), linewidth='1.0'),
    capprops=dict(color='black', linewidth=2.0),
    flierprops=dict(marker='+', markeredgecolor='blue', markersize=6))


ax2.set_xticks([1, 2, 3, 4, 5])
ax2.set_xticklabels(['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev'], rotation=20, fontdict = font)

ax2.yaxis.tick_right()

ax2.set_ylim(0.6, 1.0)

y_ticks = np.arange(0.6, 1.01, 0.05)
ax2.set_yticks(y_ticks)

ax2.set_yticklabels(ax2.get_yticks(), fontsize = 12, fontname='Times New Roman')
ax2.set_yticklabels([f'{int(y * 100)}' for y in y_ticks])

ax2.grid(True, linestyle=(0, (1, 5)), color='gray', linewidth=0.8)

ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')

#============================================================================

plt.tight_layout()
plt.show()

#plt.savefig('myplot.pdf')
#plt.close()
