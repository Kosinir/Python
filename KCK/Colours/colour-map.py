import numpy as np
import matplotlib.pyplot as plt

def read_map_data(filename):
    with open(filename, 'r') as file:
        w, h, distance = map(float, file.readline().split())
        height_map = []
        for _ in range(int(h)):
            height_map.append(list(map(float, file.readline().split())))
    return int(w), int(h), distance, np.array(height_map)

def visualize_map(height_map):
    plt.figure(figsize=(10, 6))
    plt.imshow(height_map, cmap='terrain', origin='upper')
    plt.colorbar()
    #plt.show()
    plt.savefig('colour-map.pdf')
    plt.close()

if __name__ == "__main__":
    filename = "big.dem"
    w, h, distance, height_map = read_map_data(filename)
    visualize_map(height_map)
