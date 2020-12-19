from utils import *
from itertools import product, count as iter_count
import sys

import pickle

lines = all_lines(19)
rules_end = lines.index('')
rules = lines[:rules_end]
strings = lines[rules_end+1:]

MAX_LEN = max(len(s) for s in strings)  # 96


class Rule:
    def __init__(self, s):
        id, rest = s.split(':', 1)
        self.id = id
        self.rules = []
        self.char = None
        self.compiled = None
        rest = rest.strip()
        if '"' in rest:
            self.char = rest[1]
        else:
            for rule in rest.split('|'):
                rule = rule.strip()
                self.rules.append(rule.split())

    def __str__(self):
        return f'<{self.id}, {self.char}, {self.rules}>'

    def compile(self, all_rules):
        if self.compiled:
            return self.compiled
        if self.char:
            return [self.char]

        # print(f'{self.id}', end=' ')
        compiled = []
        for rule in self.rules:
            combos = [all_rules[k].compile(all_rules) for k in rule]
            joined = [''.join(x) for x in product(*combos)]
            compiled.extend(s for s in joined if len(s) <= MAX_LEN)

        # if self.id == '8':
        #     new_compiled = set()
        #     for rule in compiled:
        #         s = rule
        #         new_compiled.add(s)
        #         while len(s) <= MAX_LEN:
        #             s += rule
        #             new_compiled.add(s)
        #     compiled = new_compiled
        # elif self.id == '11':
        #     r42 = all_rules['42'].compile(all_rules)
        #     r31 = all_rules['31'].compile(all_rules)
        #     last_compiled = compiled.copy()
        #     x = 16
        #     while x <= MAX_LEN:
        #         print(f'11: {x}')
        #         new_compiled = {a + m + b
        #                         for a in r42
        #                         for m in last_compiled
        #                         for b in r31}
        #         compiled.update(new_compiled)
        #         last_compiled = new_compiled
        #         x += 16

        self.compiled = compiled
        return compiled


def rules_from_lines(s):
    rules = {}
    for line in s.split('\n'):
        r = Rule(line)
        rules[r.id] = r
    return rules



def test_compile():
    all_rules = {
        '0': Rule('0: 1 2'),
        '1': Rule('1: "a"'),
        '2': Rule('2: 1 3 | 3 1'),
        '3': Rule('3: "b"'),
    }
    assert all_rules['0'].compile(all_rules) == ['aab', 'aba']


def test_compile2():
    rules = rules_from_lines("""0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b" """)
    assert rules['0'].compile(rules) == 'aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, ababbb'.split(', ')


# pickle.dump(RULES, open('rules.pickle', 'wb'))
# RULES = pickle.load(open('rules.pickle', 'rb'))
# print(rule0)

RULES = {r.id: r for r in [Rule(r) for r in rules]}
rule0 = RULES['0'].compile(RULES)
rule42 = RULES['42'].compile(RULES)
rule31 = RULES['31'].compile(RULES)

def rule_len(r):
    return {len(x) for x in r}


print(f'Len 42: {rule_len(rule42)}')
print(f'Len 31: {rule_len(rule31)}')


def match42(s, empty_ok=False):
    if empty_ok and not s:
        return True
    if len(s) % 8 != 0:
        return False
    for r in rule42:
        if s.startswith(r):
            return match42(s[8:], True)
    return False


def match(s, empty_ok=False):
    if empty_ok and not s:
        return True
    if len(s) % 8 != 0:
        return False
    if len(s) <= 16:
        return False
    found = False
    for r in rule31:
        if s.endswith(r):
            found = True
            break
    if found:
        if not match42(s[:8]):
            return False
        if match42(s[8:-8], True):
            return True
        else:
            return match(s[8:-8], True)
    else:
        return False


def test_match():
    assert match('aaaabaabbbbaabbbabbabbba')

#
#
count = 0
for line in strings:
    if match(line):
        count += 1
    else:
        if line in rule0:
            print(f'MISMATCH: {line}')

print('\nANSWER')
print(count)
#
# x = RULES['42'].compile(RULES)
# # print(len(x))
# # print(len(set(x)))
#
