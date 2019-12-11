import numpy as np
import matplotlib.pyplot as plt
from common import paint


def get_boundaries(points):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    return min_x, max_x, min_y, max_y


def display(ship):
    min_x, max_x, min_y, max_y = get_boundaries(ship)
    pixels = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=int)
    for p in ship:
        if ship[p] == 1:
            pixels[p[1] - min_y][p[0] - min_x] = 1
    plt.axis('off')
    plt.imshow(pixels, cmap='Greys')
    plt.show()


display(paint(1)[1])
