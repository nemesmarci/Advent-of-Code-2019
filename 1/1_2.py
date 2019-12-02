from functools import reduce


def fuel(mass):
    return mass // 3 - 2


def fuel2(mass):
    total_fuel = fuel(mass)
    added_fuel = fuel(total_fuel)
    while added_fuel > 0:
        total_fuel += added_fuel
        added_fuel = fuel(added_fuel)
    return total_fuel


with open('input.txt') as modules:
    print(reduce(lambda a, b: a + fuel2(b),
                 (int(module) for module in modules), 0))
