# There are methods of list manipulation which are quite cool.
# For example, here, u can use nrisk = [[0] * len(row) * 5 for row in risk * 5] to create a copy of risk five times in two directions

import heapq  # this module implements priority queues :D very pog

risk = []
while True:  # creating risk map
    s = input()
    if s == '': break
    risk.append(list(map(int, s)))
nrisk = [[0] * len(row) * 5 for row in risk * 5]


def mod(n):
    return (n - 1) % 9 + 1


a = len(risk)
b = len(risk[0])

for i in range(len(nrisk)):
    for j in range(len(nrisk[i])):
        nrisk[i][j] = mod(risk[i % a][j % b] + j // b + i // a)

paths = [(0, 0, 0)]  # tuple of (risk, x coord, y coord)

vis = [[0] * len(row) for row in nrisk]

while True:
    rf, x, y = heapq.heappop(paths)  # using the top of the heap, smallest risk
    if vis[x][y]:  # skip visited places
        continue
    if (x, y) == (len(nrisk) - 1, len(nrisk[x]) - 1):  # checking whether we're at the end
        print(rf)
        break
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(nrisk) > nx >= 0 <= ny < len(nrisk[0]):  # skip ungoable places
            continue
        if vis[nx][ny]:  # skip visited places
            continue
        heapq.heappush(paths, (rf + nrisk[nx][ny], nx, ny)) # add new path to heap
