from intcode import Intcode

with open('input.txt') as program:
    codes = [int(code) for code in program.read().strip().split(',')]


def search():
    ic = Intcode(codes)
    for noun in range(0, 99):
        for verb in range(0, 99):
            ic.program[1] = noun
            ic.program[2] = verb
            if ic.run() == 19690720:
                return 100 * noun + verb
            ic.reset(program=codes)


print(search())
