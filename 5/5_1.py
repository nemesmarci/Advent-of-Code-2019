from intcode import Intcode
from io import StringIO

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]

ic = Intcode(codes, input_=StringIO('8'))
ic.run()

for i in ic.output[:-1]:
    assert(i == 0)

print(ic.output[-1])
