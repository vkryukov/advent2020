from collections import namedtuple
from math import sqrt


class Point(namedtuple('Point', 'x y')):
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __abs__(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)


UP, DOWN, LEFT, RIGHT = Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)


def test_point():
    assert abs(UP + DOWN) == 0
    assert abs(LEFT + RIGHT) == 0
    assert (UP + UP + RIGHT + RIGHT + UP).manhattan() == 5
    assert len({UP, UP, DOWN, DOWN, LEFT, LEFT, RIGHT, LEFT}) == 4
    assert abs(3 * UP + 4 * LEFT) == 5
    assert (3 * UP + 7 * RIGHT + 2 * DOWN).manhattan() == (3 + 7 - 2)
