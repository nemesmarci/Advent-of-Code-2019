from common import init, start


def compare(ball, paddle):
    if ball[0] < paddle[0]:
        return -1
    elif ball[0] > paddle[0]:
        return 1
    else:
        return 0


def parse(blocks):
    area = dict()
    i = 0
    points = 0
    ball, paddle = (None, None), (None, None)

    while i < len(blocks):
        x, y = blocks[i], blocks[i + 1]
        tile = blocks[i + 2]
        if x == -1 and y == 0:
            points = tile
        else:
            area[(x, y)] = tile
        i += 3
        if tile == 4:
            ball = (x, y)
        elif tile == 3:
            paddle = (x, y)

    return points, ball, paddle


ic = init()
ic.program[0] = 2
IC = start(ic)

joystick = 0

try:
    while True:
        IC.send(joystick)
        points, ball, paddle = parse(ic.output)
        ic.output = []
        joystick = compare(ball, paddle)

except StopIteration:
    points, _, _ = parse(ic.output)

print(points)
