from common import Moons, lcm

m = Moons()
previous_values = [set(), set(), set()]
periods = [0, 0, 0]

while True:
    m.iterate()

    for i, key in enumerate((
            tuple((moon.x, moon.velocity[0]) for moon in m.moons),
            tuple((moon.y, moon.velocity[1]) for moon in m.moons),
            tuple((moon.z, moon.velocity[2]) for moon in m.moons))):

        if not periods[i]:
            if key not in previous_values[i]:
                previous_values[i].add(key)
            else:
                periods[i] = len(previous_values[i])

    if all(periods):
        break

print(lcm(*periods))
