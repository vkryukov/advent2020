
MAX = 1_000_000
N = 10_000_000

next = [None]*(MAX+1)
prev = [None]*(MAX+1)


def init_arrays(lst):
    assert len(lst) == MAX
    for i in range(len(lst) - 1):
        next[lst[i]] = lst[i + 1]
    next[lst[-1]] = lst[0]
    for i in range(1, len(lst)):
        prev[lst[i]] = lst[i - 1]
    prev[lst[0]] = lst[-1]


def init_from_string(s, complement=False):
    arr = [int(x) for x in s]
    if complement:
        arr += list(range(max(arr)+1, MAX+1))
    return init_arrays(arr)


def print_list(top, num=MAX):
    cur = top
    for _ in range(num):
        print(cur, end=" ")
        cur = next[cur]


def down(n, next1, next2, next3, max=MAX):
    n = n - 1
    while n == 0 or n == next1 or n == next2 or n == next3:
        if n == 0:
            n = max
        else:
            n = n - 1
    return n


def move(top, max=MAX):
    first = next[top]
    second = next[first]
    third = next[second]
    dest = down(top, first, second, third, max)
    dest_after = next[dest]

    next[top] = next[third]
    prev[next[third]] = top

    next[dest] = first
    prev[first] = dest
    next[third] = dest_after
    prev[dest_after] = third

    return (next[top])


# init_from_string("123487596", complement=True)
init_from_string("389125467", complement=True)
top = 3
for _ in range(N):
    top = move(top)
print(next[1], next[next[1]], next[1] * next[next[1]])
