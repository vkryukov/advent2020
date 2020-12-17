from utils import *

lines = read_lines(17)


class Cube:
    def __init__(self, lines):
        self.coords = []
        for x in range(len(lines)):
            line = lines[x]
            for y in range(len(line)):
                if line[y] == '#':
                    self.coords.append((x, y, 0))

    def neighboors(self, point):
        x, y, z = point
        count = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    if i == j == k == 0:
                        continue
                    if (x+i, y+j, z+k) in self.coords:
                        count += 1
        return count

    def iterate(self):
        new_coords = []
        for point in self.coords:
            if 2 <= self.neighboors(point) <= 3:
                new_coords.append(point)

        minmax = []
        for d in range(3):
            min_d = min(p[d] for p in self.coords) - 1
            max_d = max(p[d] for p in self.coords) + 1
            minmax.append((min_d, max_d))

        for x in range(minmax[0][0], minmax[0][1]+1):
            for y in range(minmax[1][0], minmax[1][1] + 1):
                for z in range(minmax[2][0], minmax[2][1] + 1):
                    point = (x, y, z)
                    if not point in self.coords and self.neighboors(point) == 3:
                        new_coords.append(point)

        c = Cube([])
        c.coords = new_coords
        return c


class Cube3:
    def __init__(self, lines):
        self.coords = set()
        self.neighboors_hash = {}
        for x in range(len(lines)):
            line = lines[x]
            for y in range(len(line)):
                if line[y] == '#':
                    self.coords.add((x, y, 0, 0))

    def neighboors(self, point):
        result = self.neighboors_hash.get(point)
        if result:
            return result
        x, y, z, w = point
        count = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        if i == j == k == l == 0:
                            continue
                        if (x+i, y+j, z+k, w + l) in self.coords:
                            count += 1
        self.neighboors_hash[point] = count
        return count

    def iterate(self):
        new_coords = set()
        for point in self.coords:
            if 2 <= self.neighboors(point) <= 3:
                new_coords.add(point)

        checked = {}

        for point in self.coords:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    for k in (-1, 0, 1):
                        for l in (-1, 0, 1):
                            if i == j == k == l == 0:
                                continue
                            x, y, z, w = point
                            new_point = x + i, y + j, z + k, w + l
                            if not checked.get(new_point) and \
                                    new_point not in self.coords and self.neighboors(new_point) == 3:
                                new_coords.add(new_point)
                                checked[new_point] = True

        c = Cube3([])
        c.coords = new_coords
        return c

def test_cube():
    c = Cube(""".#.
..#
###""".split('\n'))
    c1 = c.iterate()
    print(c1.coords)



c = Cube3(lines)
for _ in range(6):
    c = c.iterate()
    print(len(c.coords))




