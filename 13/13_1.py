from common import init, start

try:
    ic = init()
    start(ic)
except StopIteration:
    pass

print(
    sum(ic.output[i] == 2 for i in range(len(ic.output)) if i % 3 == 2)
)
