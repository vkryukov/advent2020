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

    def rotate(self, direction, times=1):
        x, y = self.x, self.y
        for i in range(times):
            if direction == 'L':
                x, y = -y, x
            elif direction == 'R':
                x, y = y, -x
            else:
                raise ValueError(f"Not a recognized direction: '{direction}'")
        return Point(x, y)


UP, DOWN, LEFT, RIGHT = Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)
N, S, W, E = Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)
DIRECTIONS = dict(N=N, S=S, W=W, E=E)


def test_point():
    assert abs(UP + DOWN) == 0
    assert abs(LEFT + RIGHT) == 0
    assert (UP + UP + RIGHT + RIGHT + UP).manhattan() == 5
    assert len({UP, UP, DOWN, DOWN, LEFT, LEFT, RIGHT, LEFT}) == 4
    assert abs(3 * UP + 4 * LEFT) == 5
    assert (3 * UP + 7 * RIGHT + 2 * DOWN).manhattan() == (3 + 7 - 2)
