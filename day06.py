from utils import *


count = 0
d = {}
for line in all_lines(6):
    if line == '':
        count += len(d.keys())
        d = {}
    else:
        for x in set(line):
            d[x] = True
print(count)


count = 0
d = defaultdict(int)
lines_processed = 0
for line in all_lines(6):
    if line == '':
        for x in d.keys():
            if d[x] == lines_processed:
                count += 1
        lines_processed = 0
        d = defaultdict(int)
    else:
        for x in line:
            d[x] += 1
        lines_processed += 1
print(count)


