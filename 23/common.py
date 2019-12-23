from intcode import Intcode


class Node:
    def __init__(self, address, network):
        self.address = address
        self.network = network
        self.recieved = []


class Computer(Node):
    def __init__(self, address, network):
        super().__init__(address, network)
        self.sent = []
        self.idle = False

        with open('input.txt') as program:
            codes = [int(c) for c in program.read().split(',')]
        self.ic = Intcode(codes)
        self.IC = self.ic.run()
        self.IC.send(None)
        self.IC.send(address)

    def run(self, monitor_nat=False):
        try:
            self.IC.send(self.recieved.pop(0))
            self.IC.send(self.recieved.pop(0))
            self.idle = False
        except IndexError:
            self.idle = True

        while self.ic.output:
            address, x, y = self.ic.output[:3]
            self.ic.output = self.ic.output[3:]

            if monitor_nat and address == 255:
                return y
            self.send(address, x, y)

    def send(self, address, x, y):
        if address == 255:
            self.network[address].recieved = [x, y]
        else:
            self.network[address].recieved += [x, y]


class Nat(Node):
    def __init__(self, address, network):
        super().__init__(address, network)
        self.sent = set()
        self.idle = True

    @property
    def x(self):
        return self.recieved[0]

    @property
    def y(self):
        return self.recieved[1]

    def run(self):
        if all(self.network[c].idle for c in self.network):
            if self.y in self.sent:
                return self.y
            self.sent.add(self.y)
            self.network[0].recieved += [self.x, self.y]


def create_network(nat=False):
    network = dict()
    for i in range(50):
        network[i] = Computer(i, network)

    if nat:
        network[255] = Nat(255, network)
        nat = network[255]

    for i in range(50):
        network[i].IC.send(-1)

    return network
