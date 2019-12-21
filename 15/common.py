from collections import defaultdict
from intcode import Intcode

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def left(d):
    if d == NORTH:
        return WEST
    if d == WEST:
        return SOUTH
    if d == SOUTH:
        return EAST
    if d == EAST:
        return NORTH


def right(d):
    if d == NORTH:
        return EAST
    if d == WEST:
        return NORTH
    if d == SOUTH:
        return WEST
    if d == EAST:
        return SOUTH


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return up, left, right, down


class Droid:
    def __init__(self):
        with open('input.txt') as program:
            self.codes = [int(code) for code
                          in program.read().strip().split(',')]

        self.ic = Intcode(self.codes)
        self.IC = self.ic.run()
        self.IC.send(None)

        self.ship = defaultdict(lambda: '?')
        self.x, self.y = (0, 0)

        self.oxygen = None
        self.traverse()

    def move(self, direction):
        self.IC.send(direction)
        result = self.ic.output[-1]
        self.ic.output = []

        if direction == NORTH:
            tile = (self.x, self.y - 1)
        elif direction == SOUTH:
            tile = (self.x, self.y + 1)
        elif direction == WEST:
            tile = (self.x - 1, self.y)
        elif direction == EAST:
            tile = (self.x + 1, self.y)

        if result == 0:
            self.ship[tile] = '#'

        else:
            self.x, self.y = tile
            if result == 2:
                self.oxygen = tile

        return result

    def traverse(self):
        start = self.location
        direction = NORTH
        moved = False

        while(True):
            if moved and self.location == start:
                break

            result = self.move(direction)

            if result == 0:
                direction = right(direction)
            else:
                if not moved:
                    moved = True
                direction = left(direction)

    @property
    def location(self):
        return self.x, self.y

    def BFS(self, start):
        distances = dict()
        distances[start] = 0
        queue = [start]

        while queue:
            current = queue.pop(0)
            distance = distances[current]

            for p in get_neighbours(current):
                if self.ship[p] == '#':
                    continue

                if p in distances and distances[p] < distance + 1:
                    continue

                distances[p] = distance + 1
                queue.append(p)

        return distances
