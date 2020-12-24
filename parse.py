"""Various utilities to simplify parsing of input"""
from typing import Union, Optional

from utils import Input


def split_by(s, seps: Optional[Union[str, list[str], tuple]] = None, /, maxsplit=-1, strip=True, parse_ints=True):
    """Splits S into parts split by SEPS, which should be an iterable.

    Each SEPS should be present in the input string, otherwise split_by returns None.
    Empty strings in the start and the end are ignored, to allow a convenient way to describe
    a prefix/suffix that should be cut.

    If STRIP is set (default), all spaces around each part are removed."""
    def f(s):
        if strip:
            s = s.strip()
        if parse_ints:
            try:
                return int(s)
            except ValueError:
                return s
        else:
            return s

    if isinstance(seps, (list, tuple)):
        result = []
        for sep in seps:
            try:
                i = s.index(sep)
                result.append(f(s[:i]))
                s = s[i+len(sep):]
            except ValueError:
                return None
        result.append(f(s))
    else:
        result = [f(x) for x in s.split(sep=seps, maxsplit=maxsplit)]
    if result[0] == '':
        result = result[1:]
    if result[-1] == '':
        result = result[:-1]
    return tuple(result)


def test_split_by():
    s = '14-19 h: hhfhhhhhhhhhdshgvhh'
    assert split_by(s, ['-', ' ', ': ']) == (14, 19, 'h', 'hhfhhhhhhhhhdshgvhh')
    assert split_by(s, ['-', ' ', ': '], parse_ints=False) == ('14', '19', 'h', 'hhfhhhhhhhhhdshgvhh')
    assert split_by(s, ['-', ' ', ':']) == (14, 19, 'h', 'hhfhhhhhhhhhdshgvhh')
    assert split_by(s, ['-', ' ', ':'], strip=False) == (14, 19, 'h', ' hhfhhhhhhhhhdshgvhh')

    assert split_by('nop +0', ' ') == ('nop', 0)
    assert split_by('acc -99') == ('acc', -99)

    assert split_by('1, 2, 3, 4, 5', ',') == (1, 2, 3, 4, 5)

    assert split_by('mem[29920] = 32420282', ('mem[', '] =')) == (29920, 32420282)

    assert split_by('arrival location: 33-686 or 711-960', (':', '-', 'or', '-')) == (
        'arrival location', 33, 686, 711, 960)


def test_split_from_file():
    p1, p2 = split_by(Input(22), ('Player 1:', 'Player 2:'))
    p1, p2 = split_by(p1), split_by(p2)
    assert len(p1) == len(p2) == 25
    assert p1[0] == 3
    assert p1[-1] == 49
    assert p2[0] == 8
    assert p2[-1] == 40
