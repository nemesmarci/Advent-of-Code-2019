import math
from collections import defaultdict


class Nanofactory:
    def __init__(self):
        with open('input.txt') as data:
            reactions = dict()
            for line in data:
                line = line.strip()
                start, end = line.split(' => ')
                end_amount, end_chem = end.split()
                ingredients = dict()
                for item in start.split(', '):
                    amount, chem = item.split()
                    ingredients[chem] = int(amount)
                reactions[end_chem] = [int(end_amount), ingredients]

        self.reactions = reactions
        self.chemicals = defaultdict(int)
        self.ore = 0

    def reset(self):
        self.chemicals = defaultdict(int)
        self.ore = 0

    def get_chemical(self, chem, num):
        if chem == 'ORE':
            self.ore += num
            return

        available = self.chemicals[chem]
        if available >= num:
            self.chemicals[chem] -= num
            return

        can_create = self.reactions[chem][0]
        need_to_create = num - available
        iterations = math.ceil(need_to_create / can_create)

        for c, n in self.reactions[chem][1].items():
            self.get_chemical(c, n * iterations)

        self.chemicals[chem] += can_create * iterations - num
