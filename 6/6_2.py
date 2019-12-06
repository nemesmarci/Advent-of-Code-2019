from space import read_data

objects = read_data()
src = objects['YOU']
dest = objects['SAN']


def parents(current):
    p = []
    while current.parent is not None:
        current = current.parent
        p.append(current)
    return p


print(next(i + j for i, p in enumerate(parents(src))
           for j, q in enumerate(parents(dest)) if p == q))
