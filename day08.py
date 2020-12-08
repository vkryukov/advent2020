from utils import *

program = read_lines(8)


def run(program):
    acc = 0
    counter = 0
    executed = dict()

    while True:
        if counter >= len(program):
            return acc, True
        if counter in executed.keys():
            break
        executed[counter] = True
        instr, num = program[counter].split()
        num = int(num)
        if instr == 'nop':
            counter += 1
        elif instr == 'acc':
            acc += num
            counter += 1
        elif instr == 'jmp':
            counter += num
        else:
            raise Exception

    return acc, False





def test_part1():
    assert run("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')) == 5

# print(run(read_lines(8)))

programs = [program]

for i in range(len(program)):
    p = program[:]
    if program[i].startswith('nop'):
        p[i] = 'jmp' + p[i][3:]
        programs.append(p)
    elif program[i].startswith('jmp'):
        p[i] = 'nop' + p[i][3:]
        programs.append(p)

for p in programs:
    acc, finished = run(p)
    if finished:
        print(acc)



