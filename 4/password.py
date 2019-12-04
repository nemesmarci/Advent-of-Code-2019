def read_data():
    with open('input.txt') as data:
        return [int(i) for i in data.read().split('-')]


def ascending(s):
    for j in range(1, len(s)):
        if s[j] < s[j - 1]:
            return False
    return True


def has_double(s, strict):
    digits = '123456789'
    for d in digits:
        x = s.find(2 * d)
        if not strict and x != -1:
            return True
        if x > 3 or x in range(0, 4) and s[x: x + 3] != 3 * d:
            return True
    return False


def valid_passwords(bounds, strict=False):
    n = 0
    for i in range(bounds[0], bounds[1] + 1):
        s = str(i)
        if not ascending(s):
            continue
        if not has_double(s, strict):
            continue
        n += 1
    return(n)
