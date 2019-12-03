def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def read_data():
    with open('input.txt') as wires:
        return [line.strip().split(',') for line in wires]


def parse(wires):
    pathes = {0: {}, 1: {}}
    for i, wire in enumerate(wires):
        x = 0
        y = 0
        n = 1
        for step in wire:
            direction, distance = step[0], int(step[1:])

            def generate_nodes(axis, sign):
                nonlocal n, x, y
                start = x if axis == 'x' else y
                for iterator in range(start + sign,
                                      start + sign * (distance + 1),
                                      sign):
                    node = (iterator, y) if axis == 'x' else (x, iterator)
                    if node not in pathes[i]:
                        pathes[i][node] = n
                    n += 1
                if axis == 'y':
                    y += sign * distance
                else:
                    x += sign * distance

            if direction == 'R':
                generate_nodes('x', 1)
            elif direction == 'U':
                generate_nodes('y', 1)
            elif direction == 'L':
                generate_nodes('x', -1)
            elif direction == 'D':
                generate_nodes('y', -1)
    return pathes
