from utils import *


def int_in_range(d, x, min, max):
    try:
        return min <= int(d[x]) <= max
    except:
        return False

def part2():
    count = 0
    d = {}
    for line in all_lines(4):
        if line == '':
            keys = d.keys()
            if (
                int_in_range(d, 'byr', 1920, 2002) and
                int_in_range(d, 'iyr', 2010, 2020) and
                int_in_range(d, 'eyr', 2020, 2030) and
                int_in_range(d, 'pid', 0, 999_999_999) and len(d.get('pid', '')) == 9 and
                'hgt' in keys and (
                    (d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76) or
                    (d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193)
                ) and
                d.get('ecl') in 'amb blu brn gry grn hzl oth'.split() and
                len(d.get('hcl', '')) == 7 and d['hcl'][0] == '#' and
                set(d['hcl'][1:7]).issubset('abcdef0123456789')
            ):
                count += 1
            d = {}
        else:
            for word in line.split():
                key, val = word.split(':')
                d[key] = val
    return count


def test_part2():
    assert part2() == 101
