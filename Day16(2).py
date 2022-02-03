# This part 2 was relatively poorly made, all I had to do was manually enter another function and I don't see how anyone could have done it differently
# Plus, it's really easy to do this unless you did the first part terribly
# There IS one big thing that I could've done better, which is manually putting in the hex to binary dictionary for conversion,
# there has to be some python module or function that output four bits for every single character

dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111', }
total = 0
ns = input()
s = ''
for c in ns:
    s += dict[c]

p = list(s)

pyint = int


def int(x, y=10):
    return pyint("".join(x), y)


def typeid(id, d):
    if id == 0:
        return sum(d)
    if id == 1:
        total = 1
        for datum in d:
            total *= datum
        return total
    if id == 2:
        return min(d)
    if id == 3:
        return max(d)
    if id == 5:
        return d[0] > d[1]
    if id == 6:
        return d[1] > d[0]
    if id == 7:
        return d[0] == d[1]


def operator(p):
    global total
    d = []
    # print("".join(p))
    version = int(p[:3], 2)
    p[:] = p[3:]
    # print(version)
    total += version
    id = int(p[:3], 2)
    # print(id)
    p[:] = p[3:]
    if id == 4:
        while True:
            cont = p.pop(0)
            d += p[:4]
            p[:] = p[4:]
            if cont == '0':
                return int(d, 2)
    else:
        length = p.pop(0)
        if length == '0':
            length = int(p[:15], 2)
            p[:] = p[15:]
            np = p[:length]
            p[:] = p[length:]
            while np: d.append(operator(np))
        if length == '1':
            length = int(p[:11], 2)
            p[:] = p[11:]
            for _ in range(length): d.append(operator(p))
    return typeid(id, d)


print(operator(p))
