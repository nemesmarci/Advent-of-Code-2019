from common import run

springscript = \
    'OR B T\n' \
    'AND C T\n' \
    'NOT T J\n' \
    'AND D J\n' \
    'NOT A T\n' \
    'OR T J\n'

print(run(springscript, mode='WALK'))
