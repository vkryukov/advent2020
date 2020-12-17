from utils import count as my_count, read_lines
from itertools import *

lines = read_lines(17)


class Cube:
    def __init__(self, lines, dim=4):
        self.points = set()
        self.n_counts = {}
        self.dim = dim
        for x in range(len(lines)):
            line = lines[x]
            for y in range(len(line)):
                if line[y] == '#':
                    self.points.add((x, y) + (0,) * (dim - 2))

    def surrounding(self, point):
        for shift in product((-1, 0, 1), repeat=self.dim):
            if all(s == 0 for s in shift):
                continue
            yield tuple(x + y for x, y in zip(point, shift))

    def neighboors(self, point):
        if result := self.n_counts.get(point):
            return result
        c = my_count((p in self.points) for p in self.surrounding(point))
        self.n_counts[point] = c
        return c

    def iterate(self):
        new_coords = set()
        for point in self.points:
            if 2 <= self.neighboors(point) <= 3:
                new_coords.add(point)

        checked = set()
        for point in self.points:
            for new_point in self.surrounding(point):
                if new_point not in checked and new_point not in self.points \
                        and self.neighboors(new_point) == 3:
                    new_coords.add(new_point)
                checked.add(new_point)

        c = Cube([], dim=self.dim)
        c.points = new_coords
        return c


def test_cube():
    c = Cube(""".#.
..#
###""".split('\n'), 3)
    c1 = c.iterate()
    assert len(c1.points) == 11

    c = Cube(lines, 3)
    for _ in range(6):
        c = c.iterate()
    assert len(c.points) == 391


    c = Cube(lines, 4)
    for _ in range(6):
        c = c.iterate()
    assert len(c.points) == 2264
