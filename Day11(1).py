grid = []

while True:
    s = input()
    if s == '': break
    row = list(map(int, s))
    grid.append(row)

def energy_check():
    lst = []
    for row in range(len(grid)):
        for n in range(len(grid[row])):
            if grid[row][n] > 9:
                lst.append([row, n])
    return lst


def adjacents(coord, record):
    lst = []
    for ny, nx in [(coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1] + 1), (coord[0] + 1, coord[1]), (coord[0] + 1, coord[1] - 1), (coord[0] - 1, coord[1]), (coord[0] + 1, coord[1] + 1), (coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]:
        if not len(grid) > ny >= 0 <= nx < len(grid[ny]): continue
        if record[ny][nx] == 0:
            lst.append([ny, nx])
    return lst

total = 0
for t in range(100):
    for y in range(len(grid)):
        for x in range(len(grid[y])): grid[y][x] += 1
    record = [[0]*len(row) for row in grid]
    while energy_check():
        flashes = energy_check()
        for flash in flashes:
            if record[flash[0]][flash[1]] > 0: continue
            grid[flash[0]][flash[1]] = 0
            record[flash[0]][flash[1]] += 1
            total += 1
            for increase in adjacents(flash, record): grid[increase[0]][increase[1]] += 1
print(total)