class Object:
    def __init__(self, name):
        self.name = name
        self.orbiters = set()
        self.parent = None


def read_data():
    objects = dict()
    with open('input.txt') as data:
        for line in data:
            center, orbiter = line.strip().split(')')
            for p in center, orbiter:
                if p not in objects:
                    objects[p] = Object(p)
            objects[center].orbiters.add(objects[orbiter])
            objects[orbiter].parent = objects[center]
    return objects
