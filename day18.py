from itertools import *
from utils import *

lines = read_lines(18)

class Node:
    def __init__(self, s):
        if s.startswith('('):
            i = s.index(')')
            left = Node(s[1:i])
            i += 1
        else:
            try:
                i = s.index(' ')
                left = int(s[:i])
            except ValueError:
                left = int(s)
                i = len(s)

        #  Now we have left the first operand, and i at the last parsed symbol
        if i >= len(s):
            self.left = left
            self.op = None
            self.right = None
        else:
            self.op = s[i+1]
            self.left = left
            self.right = Node(s[i+2:].strip())

    def __repr__(self):
        return f'Node({self.left=}, {self.op=}, {self.right=})'

    def value(self):
        def val(x):
            if isinstance(x, int):
                return x
            else:
                return x.value()

        if self.op is None:
            return val(self.left)
        else:
            l, r = val(self.left), val(self.right)
            pass


def find_closing_bracket(s):
    open_close = 1
    for i in range(len(s)):
        if s[i] == '(':
            open_close += 1
        elif s[i] == ')':
            open_close -= 1
            if open_close == 0:
                return i
    return None


def next_term(s):
    s = s.strip()
    if s == '':
        return None, None, None
    if s[0] == '(':
        i = find_closing_bracket(s[1:]) + 1
        first = s[1:i].strip()
        rest = s[i+1:].strip()
    else:
        if ' ' in s:
            first, rest = s.split(' ', 1)
        else:
            return s.strip(), None, None

    rest = rest.strip()
    if rest == '':
        return first, None, None

    try:
        op, second = rest.split(' ', 1)
    except ValueError:
        pass
    return first.strip(), op.strip(), second.strip()


def test_next_term():
    assert next_term('1 * 2 * 3') == ('1', '*', '2 * 3')
    assert next_term('1 * (2 * 3)') == ('1', '*', '(2 * 3)')
    assert next_term('(1 * (2 * 3)) * (4 * (5 * 6))') == ('1 * (2 * 3)', '*', '(4 * (5 * 6))')


test_next_term()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def perform_op(op, first, second):
    if op is None:
        return first
    elif op == '+':
        return first + second
    else:
        return first * second


def value(s, last_first=None, last_op=None):
    first, op, rest = next_term(s)
    try:
        first = int(first)
    except ValueError:
        first = value(first)

    lf = perform_op(last_op, first, last_first)
    if op is None:
        return lf

    return value(rest, last_first=lf, last_op=op)


def test_value():
    assert value('4') == 4
    assert value('1 + 2') == 3
    assert value('3 * 3') == 9
    assert value('(3 * 4)') == 12
    assert value('6 * 8 * (2 * 9) + 2 * 8 * 4') == (6 * 8 * 18 + 2) * 8 * 4
    assert value('9 + 6 + 8 + 2 + (6 * 4 * 6) * (9 + 7 * 6 * 5 + 5 * 3)') == (9 + 6 + 8 + 2 + 6 *4 *6) * \
        value('(9 + 7 * 6 * 5 + 5 * 3)')


def value2(s, prev=None):
    first, op, rest = next_term(s)
    try:
        first = int(first)
    except ValueError:
        first = value2(first)

    first = first + prev if prev else first
    if op is None:
        return first
    elif op == '+':
        return value2(rest, first)
    else:  # op == '*'
        return first * value2(rest)


def test_value2():
    assert value2('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert value2('2 * 3 + (4 * 5)') == 46
    assert value2('(3 + 4 + 5)') == 12
    assert value2('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    assert value2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    assert value2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

test_value2()

if __name__ == '__main__':
    print(sum(value2(line) for line in lines))
    # for line in lines:
    #     print(f'{line=}', end=' ')
    #     print(f'{value(line)}')





