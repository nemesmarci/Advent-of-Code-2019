from path import read_data, parse

wires = read_data()
pathes = parse(wires)

distances = [pathes[0][p] + pathes[1][p]
             for p in pathes[0] if p in pathes[1]]
print(min(distances))
