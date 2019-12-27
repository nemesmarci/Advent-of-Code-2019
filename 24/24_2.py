from common import Area

area = Area()

for i in range(200):
    area.iterate(recursive=True)

print(sum(1 for l in area.levels for t in area.levels[l].values() if t == '#'))
