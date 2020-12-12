from utils import *
from point import *

lines = read_lines(12)


def test_day1():
    pos = Point(0, 0)
    dir = E

    for line in lines:
        letter = line[0]
        amount = int(line[1:])
        if letter in ('N', 'S', 'E', 'W'):
            pos += DIRECTIONS[letter] * amount
        elif letter in ('L', 'R'):
            dir = dir.rotate(letter, amount // 90)
        else:  #F
            pos += dir * amount

    assert pos.manhattan() == 1496


def test_day2():
    waypoint = 10 * E + 1 * N
    pos = Point(0, 0)

    print(f'{waypoint=}')

    for line in lines:
        letter = line[0]
        amount = int(line[1:])

        if letter == 'F':
            pos = pos + amount * waypoint
        elif letter in ('N', 'S', 'E', 'W'):
            waypoint = waypoint + amount * DIRECTIONS[letter]
        elif letter in ('R', 'L'):
            waypoint = waypoint.rotate(letter, amount // 90)

    assert pos.manhattan() == 63843
