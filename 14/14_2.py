from common import Nanofactory

ORE = 1000000000000

factory = Nanofactory()
factory.get_chemical('FUEL', 1)
one_fuel = factory.ore

min_fuel = ORE // one_fuel
max_fuel = min_fuel * 2

while True:
    factory.reset()
    factory.get_chemical('FUEL', max_fuel)

    if factory.ore == ORE:
        min_fuel = max_fuel
        break
    if factory.ore < ORE:
        max_fuel = max_fuel * 2
    else:
        break

while(max_fuel - min_fuel > 1):
    middle = (min_fuel + max_fuel) // 2

    factory.reset()
    factory.get_chemical('FUEL', middle)

    if factory.ore <= ORE:
        min_fuel = middle
    else:
        max_fuel = middle

print(min_fuel)
