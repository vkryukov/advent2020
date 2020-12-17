from utils import count as my_count, read_lines
from itertools import *

lines = read_lines(17)


class Cube:
    def __init__(self, lines, dim):
        self.points = set()
        self.n_counts = {}
        self.dim = dim
        for x, line in enumerate(lines):
            for y, ch in enumerate(line):
                if ch == '#':
                    self.points.add((x, y) + (0,) * (dim - 2))

    def surrounding(self, point):
        g = product((0, -1, 1), repeat=self.dim)
        next(g)  # since it will be (0, ..., 0)
        for shift in g:
            yield tuple(x + y for x, y in zip(point, shift))

    def neighbors(self, point):
        if result := self.n_counts.get(point):
            return result
        self.n_counts[point] = my_count((p in self.points) for p in self.surrounding(point))
        return self.n_counts[point]

    def iterate(self):
        new_points = set()
        for point in self.points:
            if 2 <= self.neighbors(point) <= 3:
                new_points.add(point)

        checked = set()
        for point in self.points:
            for new_point in self.surrounding(point):
                if new_point not in checked and self.neighbors(new_point) == 3:
                    new_points.add(new_point)
                checked.add(new_point)

        c = Cube([], dim=self.dim)
        c.points = new_points
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
