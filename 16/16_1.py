from collections import defaultdict
from common import read_data

sequence = read_data()


def multiplier(n):
    first = True
    while True:
        for i in range(n):
            if first:
                first = False
                continue
            yield 0
        for i in range(n):
            yield 1
        for i in range(n):
            yield 0
        for i in range(n):
            yield -1


def iterate(sequence):
    output = []
    for i in range(len(sequence)):
        M = multiplier(i + 1)
        digits = defaultdict(int)
        for c in sequence:
            m = next(M)
            if m == 0:
                continue
            if m == 1:
                digits[c] += 1
            else:
                digits[c] -= 1
        o = sum(digits[x] * x for x in digits)
        output.append(abs(o) % 10)
    return output


for i in range(100):
    sequence = iterate(sequence)

print("".join(str(i) for i in sequence[:8]))
