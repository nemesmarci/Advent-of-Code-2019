from common import Scaffolding

s = Scaffolding()
s.scan()
intersections = []

for c in s.area:
    neighbours = s.get_neighbours(c)
    if neighbours is not None and all(s.area[n] == '#'
                                      for n in (neighbours + [c])):
        intersections.append(c)

print(sum(i[0] * i[1] for i in intersections))
