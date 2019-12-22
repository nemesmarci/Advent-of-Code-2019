from common import Beam

b = Beam()
print(sum(b.probe((x, y)) for x in range(50) for y in range(50)))
