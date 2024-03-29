from io import StringIO
from intcode import Intcode

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]

ic = Intcode(codes, input_=StringIO('5'))
ic.run()

print(ic.output[-1])
