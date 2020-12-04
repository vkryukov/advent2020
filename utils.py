# Input utilities
from math import *
from itertools import *
import pickle
import requests


def Input(n):
    n = int(n)
    filename = f'inputs/day{n:02}.txt'
    try:
        return open(filename).read()
    except FileNotFoundError:
        cookies = pickle.load(open('cookie', 'rb'))
        text = requests.get(f'https://adventofcode.com/2020/day/{n}/input', cookies=cookies).text
        open(filename, 'w').write(text)
        return text


def read_words(n): return [w for w in Input(n).split()]
def read_integers(n): return [int(w) for w in Input(n).split()]
def read_lines(n): return [s for s in Input(n).split('\n') if s != '']
def count(iterable, fn=lambda x: x): return sum(fn(x) for x in iterable)


# Arithmetic
def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result



### Tests


def test_read_integers():
    num = read_integers(1)
    assert num[11] == 1514
    assert num[57] == 1713
    assert len(num) == 200


def test_prod():
    assert prod(range(1, 10)) == factorial(9)
