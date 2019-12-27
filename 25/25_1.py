from intcode import Intcode

with open('input.txt') as data:
    codes = [int(c) for c in data.read().split(',')]

ic = Intcode(codes)
IC = ic.run()
IC.send(None)

commands = \
    'west\n' \
    'south\n' \
    'take pointer\n' \
    'north\n' \
    'east\n' \
    'east\n' \
    'south\n' \
    'south\n' \
    'take space heater\n' \
    'north\n' \
    'north\n' \
    'north\n' \
    'take wreath\n' \
    'north\n' \
    'west\n' \
    'take dehydrated water\n' \
    'north\n' \
    'east\n' \
    'south\n'

try:
    for c in commands:
        IC.send(ord(c))
except StopIteration:
    print(next(int(s) for s in ''.join(chr(c) for c in ic.output).split()
               if s.isdigit()))
