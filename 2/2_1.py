from intcode import Intcode

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]

codes[1] = 12
codes[2] = 2

ic = Intcode(codes)
print(ic.run())
