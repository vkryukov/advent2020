from utils import *

lines = read_lines(14)

print(lines[:20])


def read_mask(line):
    _, _, mask = line.split()
    return ''.join([mask[i] for i in range(len(mask)-1, -1, -1)])

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def apply_mask(value, mask):
    for i in range(len(mask)):
        if mask[i] == '0':
            value = clear_bit(value, i)
        elif mask[i] == '1':
            value = set_bit(value, i)
    return value


def apply_mask2(value, mask):
    #print(f'{value=}, {mask=}')
    for i in range(len(mask)):
        if mask[i] == '1':
            value = set_bit(value, i)
        elif mask[i] == 'X':
            new_mask = ('0' * (i+1)) + mask[i+1:]
            v1 = set_bit(value, i)
            v2 = clear_bit(value, i)
            return apply_mask2(v1, new_mask) + apply_mask2(v2, new_mask)
    return [value]

print(apply_mask2(42, 'X1001X'))


mask = ''
mem = {}

for line in lines:
    if line.startswith('mask ='):
        mask = read_mask(line)
    else:
        left_bracket = line.index('[')
        right_bracket = line.index(']')
        address = int(line[left_bracket+1:right_bracket])
        equals = line.index('=')
        value = apply_mask(int(line[equals+2:]), mask)
        mem[address] = value

print(sum(mem.values()))

def generate_masks(mask):
    for i in range(len(mask)):
        if mask[i] == 'X':
            return generate_masks(mask[:i] + '0' + mask[i+1:]) +\
                   generate_masks(mask[:i] + '1' + mask[i+1:])
    return [mask]


mem = {}
mask = ''

for line in lines:
    if line.startswith('mask ='):
        mask = read_mask(line)
    else:
        left_bracket = line.index('[')
        right_bracket = line.index(']')
        address = int(line[left_bracket+1:right_bracket])
        equals = line.index('=')
        value = int(line[equals+2:])
        for new_address in apply_mask2(address, mask):
            mem[new_address] = value

print(sum(mem.values()))
