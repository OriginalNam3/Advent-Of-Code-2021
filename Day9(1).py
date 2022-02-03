map = []

while True:
    s = input()
    if s == '':
        break
    map.append(s)

def adjacent(y, x):
    lst = [-1, -1, -1, -1]
    if y == 0 or y == len(map)-1:
        if y == 0:
            lst[1] = int(map[y + 1][x])
        if y == len(map) - 1:
            lst[0] = int(map[y-1][x])
    else:
        lst[1] = int(map[y+1][x])
        lst[0] = int(map[y - 1][x])
    if x == 0 or x == len(map[y]) - 1:
        if x == 0:
            lst[3] = int(map[y][x + 1])
        if x == len(map[y]) - 1:
            lst[2] = int(map[y][x - 1])
    else:
        lst[3] = int(map[y][x + 1])
        lst[2] = int(map[y][x - 1])
    return lst

def risklevel(map):
    risk = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            check = True
            for i in range(4):
                if adjacent(y, x)[i] < int(map[y][x]):
                    check = False
            if check:
                risk += 1+int(map[y][x])
    return risk
print(risklevel(map))