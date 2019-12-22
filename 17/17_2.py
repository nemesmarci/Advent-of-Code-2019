from common import Scaffolding

s = Scaffolding()

# Print the area to determine the traversal routine
# s.scan()
# s.display()
# s = Scaffolding()

M = 'A,B,A,B,C,A,B,C,A,C\n'
A = 'R,6,L,6,L,10\n'
B = 'L,8,L,6,L,10,L,6\n'
C = 'R,6,L,8,L,10,R,6\n'

s.ic.program[0] = 2
IC = s.ic.run()
IC.send(None)
s.ic.output = []

for c in M:
    IC.send(ord(c))
for c in A:
    IC.send(ord(c))
for c in B:
    IC.send(ord(c))
for c in C:
    IC.send(ord(c))
IC.send(ord('n'))
try:
    IC.send(ord('\n'))
except StopIteration:
    pass

print(s.ic.output[-1])
