from intcode import Intcode

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]

ic = Intcode(codes)
IC = ic.run()
IC.send(None)
IC.send(2)
print(ic.output[0])
