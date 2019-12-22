from copy import deepcopy
from collections import defaultdict


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return [up, left, right, down]


def get_diagonal(current):
    tl = (current[0] - 1, current[1] - 1)
    tr = (current[0] + 1, current[1] - 1)
    bl = (current[0] - 1, current[1] + 1)
    br = (current[0] + 1, current[1] + 1)
    return [tl, tr, bl, br]


class Explorer:
    def __init__(self, split_vaults=False):
        cave = dict()
        keys = dict()

        with open('input.txt') as data:
            lines = data.readlines()
            for y in range(len(lines)):
                for x in range(len(lines[0])):
                    c = lines[y][x]
                    cave[(x, y)] = c
                    if c.islower():
                        keys[c.upper()] = x, y
                    elif c == '@':
                        start = x, y

        if not split_vaults:
            self.starts = [start]
            self.keys = [''.join(k for k in keys)]

        else:
            self.starts = get_diagonal(start)
            for n in get_neighbours(start) + [start]:
                cave[n] = '#'
            self.keys = ['', '', '', '']
            for k in keys:
                x, y = keys[k]
                if x < start[0] and y < start[1]:
                    self.keys[0] += k
                elif x > start[0] and y < start[1]:
                    self.keys[1] += k
                elif x < start[0] and y > start[1]:
                    self.keys[2] += k
                elif x > start[0] and y > start[1]:
                    self.keys[3] += k

        self.cave = cave

    def BFS(self, current, all_keys):
        distances = defaultdict(dict)
        distances[current][''] = 0
        queue = [(current, '')]

        while queue:
            current, keys = queue.pop(0)
            distance = distances[current][keys]
            for p in get_neighbours(current):
                current_keys = deepcopy(keys)
                tile = self.cave[p]
                if tile == '#' or tile in all_keys \
                        and tile not in current_keys:
                    continue
                if tile.islower() and tile.upper() not in current_keys:
                    current_keys = ''.join(sorted(current_keys + tile.upper()))
                if current_keys in distances[p]:
                    continue
                distances[p][current_keys] = distance + 1
                queue.append((p, current_keys))
        return distances

    def solve(self):
        sum_steps = 0
        distances = [self.BFS(self.starts[i], self.keys[i])
                     for i in range(len(self.starts))]

        for i in range(len(self.starts)):
            steps = None
            d = distances[i]
            all_keys = ''.join(sorted(k for k in self.keys[i]))

            for p in d:
                if all_keys in d[p]:
                    if steps is None or d[p][all_keys] < steps:
                        steps = d[p][all_keys]

            sum_steps += steps

        return sum_steps
