from utils import *

lines = Input(16).split('\n\n')

rules, your_ticket, nearby_tickets = lines
your_ticket = read_integers(your_ticket, ',')


class Rule:
    def __init__(self, s:str):
        name, _, fields = s.partition(': ')

        self.name = name

        self.ranges = []
        for field in fields.split(' or '):
            lo, hi = field.split('-')
            self.ranges.append((int(lo), int(hi)))

    def check(self, num):
        for lo, hi in self.ranges:
            if lo <= int(num) <= hi:
                return True
        return False

    def __str__(self):
        return f'Rule< {self.name}: {self.ranges} >'

    @staticmethod
    def from_lines(lines):
        return [Rule(line) for line in lines.split('\n')]


RULES = Rule.from_lines(rules)


def part1():
    errors = 0
    for ticket in nearby_tickets.split('\n')[1:-1]:
        for field in ticket.split(','):
            field = int(field)
            if not any(r.check(field) for r in RULES):
                errors += field

    return errors


def find_positions(tickets, rules):
    valid_tickets = []
    # for ticket in tickets:
    #     correct = True
    #     for field in ticket.split(','):
    #         field_ok = False
    #         for rule in rules:
    #             if rule.check(field):
    #                 field_ok = True
    #                 break
    #         if not field_ok:
    #             correct = False
    #             break
    #     if correct:
    #         valid_tickets.append([int(f) for f in ticket.split(',')])
    valid_tickets = []
    for ticket in tickets:
        ok = True
        for field in ticket.split(','):
            field = int(field)
            if not any(r.check(field) for r in rules):
                ok = False
                break
        if ok:
            valid_tickets.append([int(f) for f in ticket.split(',')])

    positions = defaultdict(list)
    for rule in rules:
        for i in range(len(valid_tickets[0])):
            if all(rule.check(ticket[i]) for ticket in valid_tickets):
                positions[rule.name].append(i)

    return positions


def compress_positions(d: dict):
    while any(len(v) > 1 for _, v in d.items()):
        for v in d.values():
            if len(v) == 1:
                found = v[0]
                for k in d.keys():
                    if len(d[k]) > 1 and found in d[k]:
                        d[k].remove(found)
    return d



def test_find_positions():
    rules = Rule.from_lines("""class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19""")
    tickets = """3,9,18
15,1,5
5,14,9""".split('\n')

    pos = find_positions(tickets, rules)
    print(pos)


pos = find_positions(nearby_tickets.split('\n')[1:-1], RULES)
print(pos)
compressed = compress_positions(pos)
print(compressed)

final = [compressed[k][0] for k in compressed.keys() if k.startswith('departure')]
print(final)

prod = 1
my = [int(x) for x in your_ticket.split('\n')[1].split(',')]
for f in final:
    prod *= my[f]

print(prod)
# print(part1())

# positions = part2()
# print(positions)
# pos = [v for k, v in positions.items() if k.startswith('departure')]
# print(pos)

test_find_positions()