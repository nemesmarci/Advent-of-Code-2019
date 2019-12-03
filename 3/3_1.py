from path import manhattan, read_data, parse

wires = read_data()
pathes = parse(wires)

distances = [manhattan(p, (0, 0)) for p in pathes[0] if p in pathes[1]]
print(min(distances))
