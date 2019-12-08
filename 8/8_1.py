from collections import Counter
from common import read_data

layers = read_data()

counters = [Counter(layers[layer]) for layer in layers]
m = min(counters, key=lambda c: c['0'])

print(m['1'] * m['2'])
