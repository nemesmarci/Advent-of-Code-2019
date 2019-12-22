from sys import stdout
from intcode import Intcode


def read_data():
    with open('input.txt') as program:
        return [int(code) for code in program.read().strip().split(',')]


class Scaffolding:
    def __init__(self):
        self.ic = Intcode(read_data())
        self.area = dict()
        self.x_size = self.y_size = 0

    def scan(self):
        IC = self.ic.run()
        try:
            IC.send(None)
        except StopIteration:
            pass

        x, y = 0, 0
        for c in self.ic.output:
            if c != 10:
                self.area[(x, y)] = chr(c)
                x += 1
            else:
                if x != 0:
                    self.x_size = x
                x = 0
                y += 1
        self.y_size = y - 1

    def get_neighbours(self, current):
        if current[0] == 0 or current[0] == self.x_size - 1:
            return None
        if current[1] == 0 or current[1] == self.y_size - 1:
            return None
        up = (current[0], current[1] - 1)
        left = (current[0] - 1, current[1])
        right = (current[0] + 1, current[1])
        down = (current[0], current[1] + 1)
        return [up, left, right, down]

    def display(self):
        for y in range(self.y_size):
            for x in range(self.x_size):
                stdout.write(self.area[(x, y)])
            print()
