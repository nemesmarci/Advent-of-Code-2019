from intcode import Intcode


def init():
    with open('input.txt') as program:
        codes = [int(code) for code in program.read().strip().split(',')]

    ic = Intcode(codes)
    return ic


def start(ic):
    IC = ic.run()
    IC.send(None)
    return IC
