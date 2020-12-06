from utils import *


def part1():
    c = 0
    d = {}
    for line in all_lines(6):
        if line == '':
            c += len(d.keys())
            d = {}
        else:
            for x in line:
                d[x] = True
    return c


def test_part1():
    assert part1() == 6809


def part2():
    c = 0
    d = defaultdict(int)
    lines_processed = 0
    for line in all_lines(6):
        if line == '':
            c += count(d.values(), lambda x: x == lines_processed)
            lines_processed = 0
            d = defaultdict(int)
        else:
            for x in line:
                d[x] += 1
            lines_processed += 1
    return c


def test_part2():
    assert part2() == 3394



