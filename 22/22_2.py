import sympy
from common import get_data

DECK_SIZE = 119315717514047
SHUFFLES = 101741582076661


def modinv(a, m):
    x, _, g = sympy.numbers.igcdex(a, m)
    return x % m


def reverse_shuffle():
    card = sympy.Symbol('x', integer=True)
    for line in reversed(get_data()):
        if 'new' in line:
            card = DECK_SIZE - 1 - card
        else:
            n = int(line.split()[-1])
            if 'cut' in line:
                card += n
            elif 'increment' in line:
                card *= modinv(n, DECK_SIZE)
    return sympy.simplify(card % DECK_SIZE)


r = reverse_shuffle()  # (b + a * x) % m
add = r._args[0]       # b + a * x
b = int(add._args[0])  # b
mul = add._args[1]     # a * x
a = int(mul._args[0])  # a

# f(x)       =   (a * x + b) % m
# f(f(x))    = (a^2 * x + (a + 1) * b) % m
# f(f(f(x))) = (a^3 * x + (a^2 + a + 1) * b) % m
# fN(x)      = (a^N * x + (a^(N-1) + a^(N-2) + ... + a + 1) * b) % m
# fN(x)      = (a^N * x + (a^N - 1) ^% (a - 1) * b) % m

print(
    (pow(a, SHUFFLES, DECK_SIZE) * 2020
     + (pow(a, SHUFFLES, DECK_SIZE) - 1) * b
     * modinv(a - 1, DECK_SIZE)) % DECK_SIZE
)
