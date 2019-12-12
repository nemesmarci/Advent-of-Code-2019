from common import Moons, total

m = Moons()

for i in range(1000):
    m.iterate()

print(sum(total(moon) for moon in m.moons))
