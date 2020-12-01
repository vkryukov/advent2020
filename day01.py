from utils import *


def n_with_sum(numbers, target, n):
    for x in combinations(numbers, n):
        if sum(x) == target:
            return prod(x)
    return None


def test_n_with_sum():
    assert n_with_sum([1721, 979, 366, 299, 675, 1456], 2020, 2) == 1721 * 299
    assert n_with_sum([1721, 979, 366, 299, 675, 1456], 2020, 3) == 241861950


def test_part1():
    assert n_with_sum(read_integers('inputs/day01.txt'), 2020, 2) == 1016964


def test_part2():
    assert n_with_sum(read_integers('inputs/day01.txt'), 2020, 3) == 182588480
