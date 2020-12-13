from utils import *

lines = read_lines(13)

earliest = int(lines[0])

buses = [int(n) for n in lines[1].split(',') if n != 'x']

def find_optimal_bus():
    min_wait = earliest
    min_bus = 0
    for bus in buses:
        if (earliest // bus) * bus == earliest:
            return 0
        wait = ((earliest // bus) + 1) * bus - earliest
        if wait < min_wait:
            min_wait = wait
            min_bus = bus
    return min_wait * min_bus

print(find_optimal_bus())

positions = [int(n) if n != 'x' else n for n in lines[1].split(',')]
buses = [(n, positions.index(n)) for n in positions if isinstance(n, int)]

print(buses)


def extended_euclid(a, b):
    r0, s0, t0 = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r0 // r1
        r1, r0 = r0 - q * r1, r1
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1
    return s0, t0


def test_extended_euclid():
    s, t = extended_euclid(71, 15)
    assert s * 71 + t * 15 == 1


def chinese_remainders(aa, nn):
    a1, a2, *a_rest = aa
    n1, n2, *n_rest = nn
    m1, m2 = extended_euclid(n1, n2)
    a12 = (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)
    if a_rest:
        return chinese_remainders([a12] + a_rest, [n1 * n2] + n_rest)
    else:
        return a12


def test_chinese_reminders():
    assert chinese_remainders([1, 2], [3, 5]) == 7

aa = [-x[1] for x in buses]
nn = [x[0] for x in buses]

print(chinese_remainders(aa, nn))