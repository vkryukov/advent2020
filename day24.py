from parse import split_by
from utils import *
from point import Point
import math

sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))

dir = dict(
    e=Point(1, 0),
    ne=Point(cos60, sin60),
    se=Point(cos60, -sin60),
    w=Point(-1, 0),
    nw=Point(-cos60, sin60),
    sw=Point(-cos60, -sin60),
)

lines = read_lines(24)


def test_dict():
    assert dir['nw'] + dir['w'] + dir['sw'] + dir['e'] + dir['e'] == Point(0, 0)


def follow_path(line):
    start = Point(0, 0)
    while line:
        if line[0] in ('e', 'w'):
            start += dir[line[0]]
            line = line[1:]
        else:
            start += dir[line[:2]]
            line = line[2:]
    return start


def calculate_visits(lines):
    visited = defaultdict(int)
    for line in lines:
        p = follow_path(line)
        visited[p] = (visited[p] + 1) % 2
    return visited


def test_calculate_visits():
    lines = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()
    visited = calculate_visits(lines)
    sum(v for v in visited.values()) == 10

    assert follow_path('esew') == dir['se']
    assert follow_path('nwwswee') == Point(0, 0)


def test_part1():
    visited = calculate_visits(lines)
    assert sum(v for v in visited.values()) == 287


def iterate(visited, days):
    def update(p, v, visited, next_day):
        np = sum(visited.get(p + x, 0) for x in dir.values())
        if v == 1:
            if np == 0 or np > 2:
                next_day[p] = 0
            else:
                next_day[p] = 1
        else:
            if np == 2:
                next_day[p] = 1
            else:
                next_day[p] = 0

    for day in range(days):
        print(f'{day}: {len(visited.keys())}')
        next_day = {}
        for p, v in visited.items():
            update(p, v, visited, next_day)
            for x in dir.values():
                if p+x not in visited.keys() and p+x not in next_day.keys():
                    update(p+x, 0, visited, next_day)

        visited = {k: v for k, v in next_day.items() if v == 1}

    return sum(v for v in visited.values())


def test_iterate():
    lines = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()
    visited = calculate_visits(lines)
    assert iterate(visited, 1) == 15
    assert iterate(visited, 10) == 37
    assert iterate(visited, 20) == 132


def test_part2():
    visited = calculate_visits(lines)
    assert iterate(visited, 100) == 3636
