grid = []
total = 0
sizes = []
basin = []

while True:
    s = input()
    if s == '':
        break
    grid.append(s)


def adjacent(y, x):
    lst = [-1, -1, -1, -1]
    if y == 0 or y == len(grid) - 1:
        if y == 0:
            lst[1] = int(grid[y + 1][x])
        if y == len(grid) - 1:
            lst[0] = int(grid[y - 1][x])
    else:
        lst[1] = int(grid[y + 1][x])
        lst[0] = int(grid[y - 1][x])
    if x == 0 or x == len(grid[y]) - 1:
        if x == 0:
            lst[3] = int(grid[y][x + 1])
        if x == len(grid[y]) - 1:
            lst[2] = int(grid[y][x - 1])
    else:
        lst[3] = int(grid[y][x + 1])
        lst[2] = int(grid[y][x - 1])
    return lst


def lowpoints(map):
    lst = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            check = True
            for i in range(4):
                if adjacent(y, x)[i] < int(map[y][x]):
                    check = False
            if check:
                lst.append([y, x])
    return lst


def basinfind(y, x):
    coordx = x
    coordy = y
    if [y, x] not in basin:
        adjacents = adjacent(y, x)
        basin.append([y, x])
        for x in range(4):
            if adjacents[x] < 9 and adjacents[x] > 0:
                if x == 0:
                    basinfind(coordy - 1, coordx)
                if x == 1:
                    basinfind(coordy + 1, coordx)
                if x == 2:
                    basinfind(coordy, coordx - 1)
                if x == 3:
                    basinfind(coordy, coordx + 1)


for point in lowpoints(grid):
    basin = []
    basinfind(point[0], point[1])
    sizes.append(len(basin))

total = max(sizes)
sizes.remove(total)
for x in range(2):
    biggest = max(sizes)
    total *= biggest
    sizes.remove(biggest)

print(total)
