from common import Beam


def below(p):
    return p[0], p[1] + 1


def right(p):
    return p[0] + 1, p[1]


b = Beam()
current = (0, 0)

if not b.probe(below(current)) and not b.probe(right(below(current))):
    current = below(current)
    while not b.probe(current):
        current = right(current)
        if not b.probe(current):
            current = below(current)

while True:
    opposite_corner = current[0] + 99, current[1] - 99
    if opposite_corner[0] >= 0 and opposite_corner[1] >= 0:
        if b.probe(opposite_corner):
            nearest_corner = current[0], opposite_corner[1]
            print(10000 * nearest_corner[0] + nearest_corner[1])
            break

    if b.probe(below(current)):
        current = below(current)

    else:
        current = right(current)
