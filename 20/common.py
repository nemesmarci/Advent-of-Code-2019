from collections import defaultdict

AA = '%'
ZZ = '$'
# portals are represented by ascii characters starting with '0'
# leaving ' ', '#' and '.' available for other parts of the map
FIRST_PORTAL = '0'


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return [up, left, right, down]


class Explorer:
    def __init__(self, split_vaults=False):
        self.area = dict()
        portal_map = dict()
        portal_map['AA'] = AA
        portal_map['ZZ'] = ZZ
        self.portals = defaultdict(list)

        portal_id = ord(FIRST_PORTAL)

        with open('input.txt') as data:
            lines = data.readlines()
            self.y = len(lines)
            self.x = max(len(line) for line in lines) - 1
            for y in range(self.y):
                for x in range(self.x):
                    tile = lines[y][x]

                    if tile.isupper():
                        if x == 0 or x == self.x - 1 \
                                or y == 0 or y == self.y - 1:
                            tile = ' '

                        else:
                            neighbours = [lines[n[1]][n[0]]
                                          for n in get_neighbours((x, y))]

                            if '.' in neighbours:
                                if neighbours[0] == '.':
                                    portal_name = tile + neighbours[3]
                                elif neighbours[1] == '.':
                                    portal_name = tile + neighbours[2]
                                elif neighbours[2] == '.':
                                    portal_name = neighbours[1] + tile
                                else:
                                    portal_name = neighbours[0] + tile

                                if portal_name not in portal_map:
                                    portal_map[portal_name] = chr(portal_id)
                                    portal_id += 1

                                self.portals[portal_map[portal_name]] \
                                    .append((x, y))

                                tile = portal_map[portal_name]
                            else:
                                tile = ' '

                    self.area[(x, y)] = tile

        self.start = self.find_entrances('%')[0]
        self.end = self.find_entrances('$')[0]

    def find_entrances(self, portal):
        return [next(n for n in get_neighbours(t) if self.area[n] == '.')
                for t in self.portals[portal]]

    def up(self, portal):
        return portal[0] in [1, self.x - 2] \
            or portal[1] in [1, self.y - 2]

    def BFS(self, recursive=False):
        distances = defaultdict(dict)
        distances[0][self.start] = 0
        queue = [(self.start, 0)]

        while queue:
            current, level = queue.pop(0)
            if level > len(self.portals):
                continue
            current_distance = distances[level][current]

            for p in get_neighbours(current):
                tile = self.area[p]

                if tile in ['#', AA, ZZ]:
                    continue

                offset = 0
                if tile >= FIRST_PORTAL:
                    direction = self.up(p)

                    if level == 0 and direction:
                        continue

                    entrances = self.find_entrances(tile)
                    p = next(e for e in entrances if e != current)
                    if recursive:
                        offset = -1 if direction else 1

                if p in distances[level + offset] \
                        and distances[level + offset][p] \
                        < current_distance + 1:
                    continue

                distances[level + offset][p] = current_distance + 1
                queue.append((p, level + offset))

        return distances[0][self.end]
