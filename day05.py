from utils import *

lines = all_lines(5)

def row(s):
    lower, upper = 0, 127
    for c in s[:7]:
        if c == 'B':
            lower = lower + (upper - lower + 1) // 2
        else:
            upper = upper - (upper - lower + 1) // 2
    return lower

def seat(s):
    lower, upper = 0, 7
    for c in s[7:]:
        if c == 'R':
            lower = lower + (upper - lower + 1) // 2
        else:
            upper = upper - (upper - lower + 1) // 2
    return lower


def row1(s):
    return row(s), row(s) * 8 + seat(s)

def test_row():
    # assert row1('FBFBBFFRLR') == 44
    assert row('BFFFBBFRRR') == 70, 567
    assert row('FFFBBBFRRR') == 14, 119
    assert row('BBFFBBFRLL') == 102, 820

max_line = max(lines, key=lambda s: row1(s)[1])
print(row1(max_line))  # (111, 890)

all_seats = sorted([row1(s)[1] for s in lines])
for i in range(len(all_seats)-1):
    if all_seats[i+1] == all_seats[i] + 2:
        print(all_seats[i] + 1)  # 651
