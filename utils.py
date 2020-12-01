# Input utilities
from math import *
from itertools import *


def read_integers(filename): return [int(x) for x in open(filename, 'r').read().split()]

# Arithmetic
def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result


def test_read_integers():
    num = read_integers('inputs/day01.txt')
    assert num[11] == 1514
    assert num[57] == 1713
    assert len(num) == 200


def test_prod():
    assert prod(range(1, 10)) == factorial(9)