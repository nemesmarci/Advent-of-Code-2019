import copy


class Intcode:
    def __init__(self, program):
        self.program = copy.deepcopy(program)
        self.pc = 0

    @property
    def current(self):
        return self.program[self.pc]

    def add(self):
        self.program[self.program[self.pc + 3]] = (
            self.program[self.program[self.pc + 1]] +
            self.program[self.program[self.pc + 2]])
        self.pc += 4

    def mul(self):
        self.program[self.program[self.pc + 3]] = (
            self.program[self.program[self.pc + 1]] *
            self.program[self.program[self.pc + 2]])
        self.pc += 4

    def run(self):
        while(True):
            if self.current == 1:
                self.add()
            elif self.current == 2:
                self.mul()
            elif self.current == 99:
                return self.program[0]

    def reset(self, program, pc=0):
        self.pc = pc
        self.program = copy.deepcopy(program)
