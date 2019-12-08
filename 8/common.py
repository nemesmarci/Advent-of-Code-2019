from collections import defaultdict

X = 25
Y = 6


def read_data():
    with open('input.txt') as data:
        pixels = data.read().strip()

    layers = defaultdict(list)
    layer = 0
    i = 0
    for p in pixels:
        if i < X * Y:
            i += 1
        else:
            layer += 1
            i = 1
        layers[layer].append(p)

    return layers
