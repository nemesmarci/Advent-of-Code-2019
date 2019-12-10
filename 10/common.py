from copy import deepcopy
from math import gcd, atan, pi, copysign


def relative(a, b):
    return b[0] - a[0], b[1] - a[1]


def alpha(a, b):
    x, y = relative(a, b)
    offset = pi if x < 0 else 0

    t = pi / 2 if y == 0 else -atan(x / y)

    if copysign(1, t) < 0:
        t += pi

    return t + offset


class AsteroidField:
    def __init__(self):
        self.asteroids = set()

        with open('input.txt') as data:
            lines = data.readlines()
        self.max_x, self.max_y = len(lines), len(lines[0])

        for y, line in enumerate(lines):
            for x, v in enumerate(line.strip()):
                if v == '#':
                    self.asteroids.add((x, y))

        self.detected, self.base = self.find_base()

    def blocked(self, a, b):
        blocked = []
        x, y = relative(a, b)
        d = gcd(x, y)
        x, y = x // d, y // d
        i, j = b[0] + x, b[1] + y

        while i >= 0 and i <= self.max_x and j >= 0 and j <= self.max_y:
            if (i, j) in self.asteroids:
                blocked.append((i, j))
            i, j = i + x, j + y

        return blocked

    def visibles(self, point):
        visible = deepcopy(self.asteroids)
        visible.remove(point)

        for asteroid in self.asteroids:
            if asteroid == point:
                continue
            for b in self.blocked(point, asteroid):
                if b in visible:
                    visible.remove(b)

        return visible

    def find_base(self):
        n = []

        for a in self.asteroids:
            v = self.visibles(a)
            n.append((len(v), a))

        return(max(n))

    def vaporize(self):
        n = 1

        while len(self.asteroids) != 1:
            visible = sorted(self.visibles(self.base),
                             key=lambda p: alpha(self.base, p))

            for v in visible:
                if n == 200:
                    return(v[0] * 100 + v[1])
                self.asteroids.remove(v)
                n += 1
