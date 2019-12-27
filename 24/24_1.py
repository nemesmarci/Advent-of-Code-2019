from common import Area

area = Area()
seen = [area.levels]

while True:
    area.iterate()
    if area.levels in seen:
        break
    seen.append(area.levels)

print(sum(pow(2, y * 5 + x) for y in range(5) for x in range(5)
          if area.levels[0][(x, y)] == '#'))
