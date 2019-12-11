from collections import defaultdict
from intcode import Intcode

DIRECTIONS = {'up': ['left', 'right'], 'left': ['down', 'up'],
              'down': ['right', 'left'], 'right': ['up', 'down']}


def move(x, y, d):
    if d == 'up':
        y -= 1
    elif d == 'down':
        y += 1
    elif d == 'left':
        x -= 1
    elif d == 'right':
        x += 1
    return x, y


def turn(left_or_right, direction):
    return DIRECTIONS[direction][left_or_right]


def paint(start):
    with open('input.txt') as program:
        codes = [int(code) for code in program.read().strip().split(',')]

    ship = defaultdict(int)
    x, y = (0, 0)
    ship[(x, y)] = start
    direction = 'up'

    ic = Intcode(codes)
    IC = ic.run()
    IC.send(None)

    painted = set()

    while True:
        try:
            color = ship[(x, y)]
            IC.send(color)
            new_color = ic.output[-2]
            if color != new_color:
                painted.add((x, y))
            ship[(x, y)] = new_color
            left_or_right = ic.output[-1]
            direction = turn(left_or_right, direction)
            x, y = move(x, y, direction)
        except StopIteration:
            break
    return painted, ship
