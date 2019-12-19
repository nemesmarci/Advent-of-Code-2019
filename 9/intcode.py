import copy
from collections import defaultdict


class Intcode:
    def __init__(self, program):
        self.program = defaultdict(int)
        for i, p in enumerate(program):
            self.program[i] = p
        self.pc = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.output = []
        self.relative_base = 0

    def parse_instruction(self):
        instruction = str(self.current)
        length = len(instruction)
        if length < 5:
            instruction = (5 - length)*'0' + instruction
        self.a, self.b, self.c, d, e = [int(i) for i in instruction]
        return 10*d + e

    @property
    def current(self):
        return self.program[self.pc]

    def op(self, name):
        offset = self.pc + 3 - ord(name) + ord('a')
        mode = getattr(self, name)
        if mode == 0:
            return self.program[offset]
        elif mode == 1:
            return offset
        elif mode == 2:
            return self.program[offset] + self.relative_base
        else:
            print('Invalid mode:', mode)

    def add(self):
        self.program[self.op('a')] = \
            self.program[self.op('b')] + self.program[self.op('c')]
        self.pc += 4

    def mul(self):
        self.program[self.op('a')] = \
            self.program[self.op('b')] * self.program[self.op('c')]
        self.pc += 4

    def read(self, data):
        self.program[self.op('c')] = data
        self.pc += 2

    def write(self):
        self.output.append(self.program[self.op('c')])
        self.pc += 2

    def jit(self):
        if self.program[self.op('c')] != 0:
            self.pc = self.program[self.op('b')]
        else:
            self.pc += 3

    def jif(self):
        if self.program[self.op('c')] == 0:
            self.pc = self.program[self.op('b')]
        else:
            self.pc += 3

    def lt(self):
        self.program[self.op('a')] = 1 if \
            self.program[self.op('c')] < self.program[self.op('b')] else 0
        self.pc += 4

    def eq(self):
        self.program[self.op('a')] = 1 if \
            self.program[self.op('c')] == self.program[self.op('b')] else 0
        self.pc += 4

    def rbo(self):
        self.relative_base += self.program[self.op('c')]
        self.pc += 2

    def run(self):
        while(True):
            if self.current == 99:
                return self.program[0]
            opcode = self.parse_instruction()
            if opcode == 1:
                self.add()
            elif opcode == 2:
                self.mul()
            elif opcode == 3:
                data = yield
                self.read(data)
            elif opcode == 4:
                yield self.write()
            elif opcode == 5:
                self.jit()
            elif opcode == 6:
                self.jif()
            elif opcode == 7:
                self.lt()
            elif opcode == 8:
                self.eq()
            elif opcode == 9:
                self.rbo()
            else:
                print('Invalid instruction:', self.current)
                break

    def reset(self, program, pc=0):
        self.program = defaultdict(int)
        for i, p in enumerate(program):
            self.program[i] = p
        self.pc = pc
        self.a, self.b, self.c = 0, 0, 0
        self.output = []
