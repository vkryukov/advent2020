from utils import *

trees = read_lines('inputs/day03.txt')

def value(line, i):
    i = i % len(line)
    return 1 if line[i] == '#' else 0

def calc(slope, step = 1):
    index = 0
    count = 0
    for i in range(step, len(trees), step):
        index += slope
        count += value(trees[i], index)
    return count


def test_part1():
    assert calc(3) == 178


def test_part2():
    assert calc(1) * calc(3) * calc(5) * calc(7) * calc(1, 2) == 3492520200
