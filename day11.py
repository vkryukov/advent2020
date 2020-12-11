import itertools
from utils import *

lines = read_lines(11)

print(lines[:15])

seats = []

FLOOR, EMPTY, OCCUPIED = range(3)


class Seats:
    def __init__(self, lines):
        if len(lines) == 0:
            return
        self.seats = []
        self.height = len(lines)
        self.width = len(lines[0])
        for line in lines:
            for chair in line:
                if chair == 'L':
                    self.seats.append(EMPTY)
                elif chair == '#':
                    self.seats.append(OCCUPIED)
                else:
                    self.seats.append(FLOOR)

    def status(self, h, w):
        if not (0 <= h < self.height):
            return None
        if not (0 <= w < self.width):
            return None
        return self.seats[h * self.width + w]

    def neighbors(self, h, w, max=1):
        seats = []
        for delta_h, delta_w in [(-1, -1), (-1, 0), (-1, 1),
                                 (0, 1), (0, -1),
                                 (1, -1), (1, 0), (1, 1)]:
            for i in itertools.count(1):
                if i > max:
                    break
                hh = h + delta_h * i
                ww = w + delta_w * i
                stat = self.status(hh, ww)
                if stat is None:
                    break
                elif stat != FLOOR:
                    seats.append(stat)
                    break
        return Counter(seats).get(OCCUPIED, 0)

    def __eq__(self, other):
        return self.seats == other.seats

    def transform(self, max=1, limit=4):
        s = Seats([])
        s.width = self.width
        s.height = self.height
        s.seats = self.seats[:]

        for h in range(self.height):
            for w in range(self.width):
                stat = self.status(h, w)
                neighbors = self.neighbors(h, w, max)
                if stat == EMPTY and neighbors == 0:
                    s.seats[h * self.width + w] = OCCUPIED
                elif stat == OCCUPIED and neighbors >= limit:
                    s.seats[h * self.width + w] = EMPTY
        return s

    def transform_forever(self, max=1, limit=4):
        s = self
        s1 = self.transform(max, limit)
        while s1 != s:
            s = s1
            s1 = s.transform(max, limit)
        return s

    def counter(self):
        return Counter(self.seats)


def test_transform():
    inp = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    s = Seats(inp)
    expected_empty = Counter(inp)["L"]
    assert s.counter()[OCCUPIED] == 0
    assert s.counter()[EMPTY] == expected_empty
    empty = s.counter()[EMPTY]
    s = s.transform()
    assert s.counter()[OCCUPIED] == empty


lines = read_lines(11)

print(lines[:10])

s = Seats(lines).transform_forever()
c = Counter(s.seats)
print(c.get(OCCUPIED, 0))

s = Seats(lines).transform_forever(100_000_000, 5)
c = Counter(s.seats)
print(c.get(OCCUPIED, 0))
