from utils import *

import sys

def spoken(numbers):
    mem = {}

    def set_item(key, val):
        nonlocal mem
        last = mem.get(key)
        if last:
            mem[key] = (val, last[0])
        else:
            mem[key] = (val,)

    for i in range(len(numbers)):
        num = numbers[i]
        set_item(num, i)

    counter = len(numbers)
    last = numbers[-1]
    while True:
        spoken = mem.get(last)
        if spoken and len(spoken) >= 2:
            num = spoken[0] - spoken[1]
        else:
            num = 0
        set_item(num, counter)
        last = num
        counter += 1
        yield num


def spoken_at(numbers, position):
    times = position - len(numbers) - 1
    g = spoken(numbers)
    for _ in range(times):
        next(g)
    return next(g)


print(spoken_at([1,0,18,10,19,6], int(sys.argv[1])))
