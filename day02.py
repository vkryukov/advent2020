from utils import *


def parse_line(s):
    region, letter, password = s.split()
    lo, hi = region.split('-')
    lo, hi = int(lo), int(hi)
    letter = letter[0]
    return lo, hi, letter, password


def valid(s):
    lo, hi, letter, password = parse_line(s)
    return lo <= password.count(letter) <= hi


def valid2(s):
    lo, hi, letter, password = parse_line(s)
    return count([password[lo - 1] == letter, password[hi - 1] == letter]) == 1


def test_part1():
    assert count(read_lines(2), valid) == 580


def test_part2():
    assert count(read_lines(2), valid2) == 611
