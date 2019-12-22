from intcode import Intcode


class Beam:
    def __init__(self):
        with open('input.txt') as program:
            codes = [int(code) for code in program.read().strip().split(',')]
        self.codes = codes
        self.ic = Intcode(codes)

    def probe(self, point):
        self.ic.reset(self.codes)
        IC = self.ic.run()
        IC.send(None)
        IC.send(point[0])
        try:
            IC.send(point[1])
        except StopIteration:
            return self.ic.output[-1]
