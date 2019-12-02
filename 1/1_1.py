from functools import reduce


def fuel(mass):
    return mass // 3 - 2


with open('input.txt') as modules:
    print(reduce(lambda a, b: a + fuel(b),
                 (int(module) for module in modules), 0))
