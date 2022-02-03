lst = []
while True:
    s = input()
    if s == '':
        break
    lst.append(s)

temp1 = temp2 = lst[:]
for x in range(12):
    c = [0, 0]
    temp1 = temp2
    if len(temp1) > 1:
        temp2 = []
        for y in range(len(temp1)):
            if temp1[y][x] == '0':
                c[0] += 1
            if temp1[y][x] == '1':
                c[1] += 1
        if c[0] == c[1]:
            index = '1'
        else:
            index = str(c.index(max(c)))
        for y in range(len(temp1)):
            if temp1[y][x] == index:
                temp2.append(temp1[y])

print(int(temp2[0], 2))

temp1 = temp2 = lst[:]
for x in range(12):
    c = [0, 0]
    temp1 = temp2
    if len(temp1) > 1:
        temp2 = []
        for y in range(len(temp1)):
            if temp1[y][x] == '0':
                c[0] += 1
            if temp1[y][x] == '1':
                c[1] += 1
        if c[0] == c[1]:
            index = '1'
        else:
            index = str(c.index(max(c)))
        for y in range(len(temp1)):
            if temp1[y][x] != index:
                temp2.append(temp1[y])

print(int(temp2[0], 2))