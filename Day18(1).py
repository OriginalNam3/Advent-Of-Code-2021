# This was a long one, mainly because I misunderstood a lot of what the task said.
# However, I've gotten better at recursive functions and splitting the task into functions in general.
# Hardest part for me was figuring out how to represent the snailfish numbers.
# I just decided to make the input into a list with all integers as int and punctation as strings
# The map function is quite cool but it probably wasn't the best way to represent the snailfish numbers.
# One alternative I can think of is to define a class for snailfish numbers but I don't know what attributes and methdos to give it.
# I would have just ended up creating a class for the exact type of list I used. :(

import math # For math.ceil() which rounds up and math.floor() which rounds down

snlst = []


def sn(c):
    if c in ['[', ']', ',']: return c
    if c.isdigit(): return int(c)


while True:
    s = input()
    if s == '': break
    snlst.append(list(map(sn, s)))


def add(x, y):
    n = ['[']
    for c in x:
        n.append(c)
    n.append(',')
    for c in y:
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
                    if j == len(n)-1: return n


def magnitude(n):
    if len(n) == 2: return n[0]
    if len(n) == 5: return 3 * n[1] + 2 * n[3]
    else:
        pair = 0
        for x in range(1, len(n) - 1):
            if n[x] == '[': pair += 1
            if n[x] == ']': pair -= 1
            if pair == 0 and n[x] == ',': return 3 * magnitude(n[1:x]) + 2 * magnitude(n[x + 1:len(n) - 1])


fsn = snlst[0]

for x in range(1, len(snlst)):
    fsn = add(fsn, snlst[x])
    reduce(fsn)

print(magnitude(fsn))
