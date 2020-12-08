from utils import *

lines = all_lines(7)


def parse_line(line):
    target, others = line.split(' contain ')
    target = target.removesuffix(' bags')
    other_bags = []
    if others != 'no other bags.':
        for other in others.split(', '):
            c, first, second, _ = other.split()
            other_bags.append((int(c), first + ' ' + second))
    return target, other_bags


def test_parse_line():
    result = parse_line('dark orange bags contain 3 bright white bags, 4 muted yellow bags.')
    assert result == ('dark orange',
                      [(3, 'bright white'),
                       (4, 'muted yellow')])

d = {}
for target, others in [parse_line(line) for line in read_lines(7)]:
    d[target] = [other for _, other in others]

applicable = {'shiny gold'}
so_far = 0

TARGET = 'shiny gold'

while True:
    for bag, contains in d.items():
        candidates = set()
        for a in applicable:
            if a in contains:
                candidates.add(bag)
        applicable |= candidates
    if len(applicable) == so_far:
        break
    else:
        so_far = len(applicable)

def test_part1():
    assert len(applicable)-1 == 332

d = {target: others for target, others in [parse_line(line) for line in read_lines(7)]}

def total_cost(bag):
    total = 0
    if len(d[bag]) == 0:
        return 0
    for cost, other_bag in d[bag]:
        total += cost + cost * total_cost(other_bag)
    return total


def test_part2():
    assert total_cost(TARGET) == 10875
