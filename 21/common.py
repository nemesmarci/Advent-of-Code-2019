from intcode import Intcode


def run(springscript, mode):
    with open('input.txt') as program:
        codes = [int(code) for code in program.read().strip().split(',')]

    ic = Intcode(codes)
    IC = ic.run()
    IC.send(None)

    for c in springscript:
        IC.send(ord(c))

    for c in mode:
        IC.send(ord(c))

    try:
        IC.send(ord('\n'))
    except StopIteration:
        return ic.output[-1]
