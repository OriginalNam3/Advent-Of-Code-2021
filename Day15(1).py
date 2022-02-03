# had to look up priority queues and found very useful heapq module
# Not very familiar with these types of searching algorithms, so I learnt a lot

import heapq  # this module implements priority queues :D very pog

risk = []
while True:  # creating risk map
    s = input()
    if s == '':
        break
    risk.append(list(map(int, s)))

paths = [(0, 0, 0)]  # tuple of (risk, x coord, y coord) as a heap

vis = [[0] * len(row) for row in risk]

while True:
    rf, x, y = heapq.heappop(paths)  # using the top of the heap, smallest risk
    print(rf)
    if vis[x][y]:  # skip visited places
        continue
    if (x, y) == (len(risk) - 1, len(risk[x]) - 1):  # checking whether we're at the end
        print(rf)
        break
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) > nx >= 0 <= ny < len(risk[0]):  # skip ungoable places
            continue
        if vis[nx][ny]:  # skip visited places as this is already lowest risk, I actually didn't even think of this
            continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))

# graph = []
# while True:
#     s = input()
#     if s == '':
#         break
#     graph.append(s)
#
# vis = [[0] * len(row) for row in graph]
# print(vis)
#
# new = [0]
# for x in range(len(graph)-1):
#     new.append(horizontal_risk(0, 1, x+1))
# print(new)
#
# for row in range(len(graph)):
#     new = optimalpath(row, new)
#     print(new)
#
# print(new[len(graph[0])-1]-int(graph[0][0]))
#
# lowest_risk = new[len(graph[0])-1]

# def paths(y, x, risk, travelled):
#     print(y, x, travelled)
#     global lowest_risk
#     print(lowest_risk)
#     if risk > 400:
#         return
#     new_travelled = travelled.copy()
#     new_travelled.append([y, x])
#     y_coord = y
#     x_coord = x
#     new_risk = risk + int(graph[y][x])
#     if y == len(graph)-1 and x == len(graph[0])-1:
#         if new_risk < lowest_risk:
#             lowest_risk = new_risk
#             print(lowest_risk)
#         return
#     if x > 0:
#         if [y_coord, x_coord - 1] not in travelled:
#             paths(y_coord, x_coord - 1, new_risk, new_travelled)
#     if x < len(graph[0]) - 1:
#         if [y_coord, x_coord + 1] not in travelled:
#             paths(y_coord, x_coord + 1, new_risk, new_travelled)
#     if y_coord < len(graph)-1:
#         if [y_coord + 1, x_coord] not in travelled:
#             paths(y_coord + 1, x_coord, new_risk, new_travelled)
#     if y_coord > 0:
#         if [y_coord - 1, x_coord] not in travelled:
#             paths(y_coord - 1, x_coord, new_risk, new_travelled)
#
# paths(0, 0, 0, [])
# print(lowest_risk - int(graph[0][0]))
#

# last_row = []
# for x in range(len(graph)-1):
#     risk = new[x]
#     last_row.append(risk + horizontal_risk(len(graph)-1, x, len(graph[0])-2))
