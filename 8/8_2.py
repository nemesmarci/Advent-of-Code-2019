import numpy as np
import matplotlib.pyplot as plt
from common import read_data, X, Y

layers = read_data()

pixels = np.zeros((Y, X), dtype=int)
for y in range(Y):
    for x in range(X):
        for layer in layers:
            current = layers[layer][y * X + x]
            if current == '2':
                continue
            pixels[y][x] = current
            break

plt.imshow(pixels, cmap='Greys')
plt.show()
