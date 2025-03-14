import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Wczytaj dane z plików CSV
c1 = pd.read_csv('1c.csv')
crs1 = pd.read_csv('1crs.csv')
ers1 = pd.read_csv('1ers.csv')
c2 = pd.read_csv('2c.csv')
crs2 = pd.read_csv('2crs.csv')

# Funkcja do pobrania ostatniego wiersza kolumn z wynikami
def last_row_results(data):
    return data.iloc[-1, 2:].dropna()

# Pobierz dane z ostatniego wiersza dla każdego zestawu danych
data_c1 = last_row_results(c1)
data_crs1 = last_row_results(crs1)
data_ers1 = last_row_results(ers1)
data_c2 = last_row_results(c2)
data_crs2 = last_row_results(crs2)

# Przygotuj dane do wykresu pudełkowego
data_to_plot = [data_ers1, data_crs1, data_crs2, data_c1, data_c2]

# Tworzenie wykresu pudełkowego
fig, xy = plt.subplots(figsize=(6, 8))
box = xy.boxplot(
    data_to_plot, patch_artist=True, notch=True, showmeans=True, meanline=False, widths=0.35,
    boxprops=dict(color='blue', facecolor='none'),
    medianprops=dict(color='red'),
    meanprops=dict(marker='o', markerfacecolor='blue', markeredgecolor='black'),
    whiskerprops=dict(color='blue', linestyle=(0,(10,3)), linewidth='1.0'),
    capprops=dict(color='black'),
    flierprops=dict(marker='+', markeredgecolor='blue',markersize=6))

# Ustawienia osi
plt.xticks([1, 2, 3, 4, 5], ['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev'], rotation=30)

xy.yaxis.tick_right()


# Ustawienia osi Y
xy.set_ylim(0.6, 1.0)  # Zakres osi Y
y_ticks = np.arange(0.6, 1.01, 0.05)  # Ticki od 0.6 do 1.0 co 0.05
xy.set_yticks(y_ticks)
xy.set_yticklabels([f'{int(y*100)}' for y in y_ticks])  # Etykiety osi Y

# Dodaj linie przerywane dla osi X i Y
plt.grid(True, linestyle=(0,(1,5)), color='gray', linewidth=0.8)

xy.tick_params(axis='x', direction='in')
xy.tick_params(axis='y', direction='in')

# Pokaż wykres
plt.tight_layout()
plt.show()
