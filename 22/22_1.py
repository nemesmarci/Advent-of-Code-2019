from common import get_data

DECK_SIZE = 10007

cards = [n for n in range(DECK_SIZE)]


def deal(cards):
    return cards[::-1]


def cut(cards, n):
    c = cards[:n]
    return cards[n:] + c


def increment(cards, n):
    len_ = len(cards)
    c = [None] * len_
    pos = 0
    for i in range(len_):
        c[pos] = cards[i]
        pos += n
        pos %= len_
    return c


def shuffle(cards):
    for line in get_data():
        if 'new' in line:
            cards = deal(cards)
        elif 'cut' in line:
            n = int(line.split()[-1])
            cards = cut(cards, n)
        elif 'increment' in line:
            n = int(line.split()[-1])
            cards = increment(cards, n)
    return cards


print(shuffle(cards).index(2019))
