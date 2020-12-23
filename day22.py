from utils import *


def parse():
    inp = read_lines(22)
    i = inp.index("Player 2:")
    return tuple(int(x) for x in inp[1:i]), tuple(int(x) for x in inp[i+1:])


def test_parse():
    p1, p2 = parse()
    assert p1[0] == 3
    assert p1[-1] == 49
    assert p2[0] == 8
    assert p2[-1] == 40


def move(p1, p2):
    if not p1 or not p2:
        return p1, p2

    if p1[0] > p2[0]:
        return p1[1:] + (p1[0], p2[0]), p2[1:]
    else:
        return p1[1:], p2[1:] + (p2[0], p1[0])


def score(p):
    n = len(p)
    return sum(v * (n - i) for i, v in enumerate(p))


def test_move():
    p1 = (9, 2, 6, 3, 1)
    p2 = (5, 8, 4, 7, 10)

    p1, p2 = move(p1, p2)
    assert p1 == (2, 6, 3, 1, 9, 5)
    assert p2 == (8, 4, 7, 10)

    p1, p2 = move(p1, p2)
    assert p1 == (6, 3, 1, 9, 5)
    assert p2 == (4, 7, 10, 8, 2)


def test_ends_after_29_moves():
    p1 = (9, 2, 6, 3, 1)
    p2 = (5, 8, 4, 7, 10)

    for _ in range(29):
        p1, p2 = move(p1, p2)

    assert not p1
    assert p2 == (3, 2, 10, 6, 8, 5, 9, 4, 7, 1)

    assert score(p2) == 306


def test_part1():
    p1, p2 = parse()
    while p1 and p2:
        p1, p2 = move(p1, p2)

    s = score(p1) if p1 else score(p2)
    assert s == 32272


games = defaultdict(dict)


def play(round, p1, p2):
    while True:
        if games[round].get((p1, p2)):
            return p1 + p2, tuple()
        if not p1 or not p2:
            return p1, p2
        games[round][((p1, p2))] = True
        c1, c2 = p1[0], p2[0]
        first_won = False
        if c1 <= len(p1)-1 and c2 <= len(p2) - 1:
            # Recursive combat
            games[round+1] = {}
            rp1, rp2 = play(round+1, p1[1:c1+1], p2[1:c2+1])
            if not rp2:
                first_won = True
        else:
            first_won = c1 > c2
        if first_won:
            p1, p2 = p1[1:]+(c1, c2), p2[1:]
        else:
            p1, p2 = p1[1:], p2[1:]+(c2, c1)


def test_play():
    p1, p2 = (9, 2, 6, 3, 1), (5, 8, 4, 7, 10)
    p1, p2 = play(1, p1, p2)
    assert not p1
    assert p2 == (7, 5, 6, 2, 4, 1, 10, 8, 9, 3)

    p1, p2 = parse()
    p1, p2 = play(1, p1, p2)
    assert score(p1) == 33206
