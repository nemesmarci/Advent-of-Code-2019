from itertools import permutations
from intcode import Intcode

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]

results = []
for p in permutations([5, 6, 7, 8, 9]):
    ic_a = Intcode(codes)
    ic_b = Intcode(codes)
    ic_c = Intcode(codes)
    ic_d = Intcode(codes)
    ic_e = Intcode(codes)

    A = ic_a.run()
    A.send(None)
    B = ic_b.run()
    B.send(None)
    C = ic_c.run()
    C.send(None)
    D = ic_d.run()
    D.send(None)
    E = ic_e.run()
    E.send(None)

    ic_e.output.append(0)

    try:
        while True:
            a = ic_e.output[-1]
            A.send(p[0])
            A.send(a)

            b = ic_a.output[-1]
            B.send(p[1])
            B.send(b)

            c = ic_b.output[-1]
            C.send(p[2])
            C.send(c)

            d = ic_c.output[-1]
            D.send(p[3])
            D.send(d)

            e = ic_d.output[-1]
            E.send(p[4])
            E.send(e)
            results.append(ic_e.output[-1])

    except StopIteration:
        pass

print(max(results))
