from copy import deepcopy


def read_data():
    tiles = dict()

    with open('input.txt') as data:
        lines = data.readlines()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                tiles[(x, y)] = c

    return tiles


def neighbours(location):
    x, y = location
    return (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)


def create_level():
    level = dict()
    for y in range(5):
        for x in range(5):
            level[(x, y)] = '.'
    return level


class Area:
    def __init__(self):
        self.levels = dict()
        self.levels[0] = read_data()
        self.levels[-1] = create_level()
        self.levels[1] = create_level()

    def sum_neighbours(self, location, level, new_levels, recursive):
        bugs = 0

        for n in neighbours(location):
            if recursive and n[0] == 2 and n[1] == 2:
                if level + 1 not in self.levels:
                    new_levels[level + 1] = create_level()
                    continue

                if location == (1, 2):
                    bugs += sum(1 for y in range(5)
                                if self.levels[level + 1][(0, y)] == '#')

                elif location == (3, 2):
                    bugs += sum(1 for y in range(5)
                                if self.levels[level + 1][(4, y)] == '#')

                elif location == (2, 1):
                    bugs += sum(1 for x in range(5)
                                if self.levels[level + 1][(x, 0)] == '#')

                elif location == (2, 3):
                    bugs += sum(1 for x in range(5)
                                if self.levels[level + 1][(x, 4)] == '#')

            elif n[0] >= 0 and n[1] >= 0 and n[0] < 5 and n[1] < 5:
                if self.levels[level][n] == '#':
                    bugs += 1

            elif recursive:
                if level - 1 not in self.levels:
                    new_levels[level - 1] = create_level()
                    continue

                if n[0] < 0 and self.levels[level - 1][(1, 2)] == '#' or \
                        n[0] > 4 and self.levels[level - 1][(3, 2)] == '#' or \
                        n[1] < 0 and self.levels[level - 1][(2, 1)] == '#' or \
                        n[1] > 4 and self.levels[level - 1][(2, 3)] == '#':
                    bugs += 1

        return bugs

    def iterate(self, recursive=False):
        new_levels = dict()

        for level in self.levels:
            tiles = self.levels[level]
            new_tiles = deepcopy(tiles)

            for location in tiles:
                if recursive and location == (2, 2):
                    continue

                tile = tiles[location]
                bugs = self.sum_neighbours(location, level,
                                           new_levels, recursive)

                if tile == '#' and bugs != 1:
                    new_tiles[location] = '.'

                elif tile == '.' and bugs in (1, 2):
                    new_tiles[location] = '#'

            new_levels[level] = new_tiles

        self.levels = new_levels
