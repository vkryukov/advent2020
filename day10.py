from utils import *


def diff(nums):
    return [nums[i] - nums[i-1] for i in range(1, len(nums))]


nums = read_integers(10)
jolts = [0] + sorted(nums) + [max(nums) + 3]
diffs = diff(jolts)


def test_day1():
    c = Counter(diff(jolts))
    assert c[3] * c[1] == 2263


conseq_values = {}


def conseq(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if n not in conseq_values:
            conseq_values[n] = conseq(n-1) + conseq(n-2) + conseq(n-3)
        return conseq_values[n]


def number(diffs):
    count = 1
    for k, g in groupby(diffs, lambda x: x):
        if k == 1:
            count *= conseq(len(list(g)))
    return count


def test_day2():
    assert number(diffs) == 396857386627072
