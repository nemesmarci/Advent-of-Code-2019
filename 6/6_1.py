from space import read_data

objects = read_data()
root = objects['COM']


def traverse(current, level=1):
    n = len(current.orbiters) * level
    for child in current.orbiters:
        n += traverse(child, level + 1)
    return n


print(traverse(root))
