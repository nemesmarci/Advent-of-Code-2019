import re
from copy import deepcopy
from math import gcd
from itertools import combinations


class Moon:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.velocity = [0, 0, 0]


class Moons:
    def __init__(self):
        self.moons = read_data()

    def iterate(self):
        prev = deepcopy(self.moons)

        for a, b in combinations((0, 1, 2, 3), 2):
            if prev[a].x < prev[b].x:
                self.moons[a].velocity[0] += 1
                self.moons[b].velocity[0] -= 1
            elif prev[a].x > prev[b].x:
                self.moons[a].velocity[0] -= 1
                self.moons[b].velocity[0] += 1

            if prev[a].y < prev[b].y:
                self.moons[a].velocity[1] += 1
                self.moons[b].velocity[1] -= 1
            elif prev[a].y > prev[b].y:
                self.moons[a].velocity[1] -= 1
                self.moons[b].velocity[1] += 1

            if prev[a].z < prev[b].z:
                self.moons[a].velocity[2] += 1
                self.moons[b].velocity[2] -= 1
            elif prev[a].z > prev[b].z:
                self.moons[a].velocity[2] -= 1
                self.moons[b].velocity[2] += 1

        for moon in self.moons:
            moon.x += moon.velocity[0]
            moon.y += moon.velocity[1]
            moon.z += moon.velocity[2]


def read_data():
    moons = []
    regex = re.compile(r"<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>")
    with open('input.txt') as data:
        for line in data:
            moons.append(Moon(*(int(i) for i in regex.match(line).groups())))
    return moons


def pot(moon):
    return sum(abs(c) for c in (moon.x, moon.y, moon.z))


def kin(moon):
    return sum(abs(v) for v in moon.velocity)


def total(moon):
    return pot(moon) * kin(moon)


def lcm(a, b, c):
    return a * b // gcd(a, b) * c // gcd(b, c)
