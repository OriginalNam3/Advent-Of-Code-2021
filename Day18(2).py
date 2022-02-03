# Again, second part is easy if functions are well defined in the first part.
# Just have to find max magnitude of all combinations of sums of snail numbers

import math

snlst = []


def sn(c):
    if c in ['[', ']', ',']: return c
    if c.isdigit(): return int(c)


while True:
    s = input()
    if s == '': break
    snlst.append(list(map(sn, s)))


def add(a, b):
    n = ['[']
    for c in a:
        n.append(c)
    n.append(',')
    for c in b:
        n.append(c)
    n.append(']')
    return n


def explode(n, i):
    for c in range(i, -1, -1):
        if isinstance(n[c], int):
            n[c] += n[i + 1]
            break
    for c in range(i + 4, len(n)):
        if isinstance(n[c], int):
            n[c] += n[i + 3]
            break
    for _ in range(4): n.pop(i)
    n[i] = 0


def split(n, i):
    temp = n.pop(i)
    n.insert(i, ']')
    n.insert(i, math.ceil(temp / 2))
    n.insert(i, ',')
    n.insert(i, math.floor(temp / 2))
    n.insert(i, '[')


def reduce(n):
    while True:
        pair = 0
        for i in range(len(n)):
            if n[i] == '[': pair += 1
            if pair == 5:
                explode(n, i)
                break
            if n[i] == ']': pair -= 1
            if i == len(n) - 1:
                for j in range(len(n)):
                    if isinstance(n[j], int) and n[j] > 9:
                        split(n, j)
                        break
                    if j == len(n) - 1: return n


def magnitude(n):
    if len(n) == 1: return n[0]
    if len(n) == 5: return 3 * n[1] + 2 * n[3]
    else:
        pair = 0
        for x in range(1, len(n) - 1):
            if n[x] == '[': pair += 1
            if n[x] == ']': pair -= 1
            if pair == 0 and n[x] == ',':
                return 3 * magnitude(n[1:x]) + 2 * magnitude(n[x + 1:len(n) - 1])


m = []

for x in range(len(snlst)):
    for y in range(len(snlst)):
        if x != y:
            rn = add(snlst[x], snlst[y])
            reduce(rn)
            m.append(magnitude(rn))
print(max(m))
