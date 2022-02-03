# Solation is rly slow.
# However, I don't know how I could do it faster so :).
# I learned another cool data representation format: sets.
# Sets have no definite order but u can still map and sort them into lists.
# A good thing is that they have no duplicate elements, so if u add an element to it that's already there, there won't be two in the set.

r = []  # List of ranges.
sd = [set() for _ in range(3)]


while True:
    s = input()
    if s == '': break
    v, s = s.split()
    state = v == 'on'
    d = [list(map(int, u[2:].split(".."))) for u in s.split(",")]
    for i in range(3):
        d[i][1] += 1
    r.append([state, d])


for i in range(3):
    for _, nr in r:
        sd[i].add(nr[i][0])
        sd[i].add(nr[i][1])


sd = list(map(sorted, sd))

xm = {x: i for i, x in enumerate(sd[0])}
# print(xm)
xy = {y: j for j, y in enumerate(sd[1])}
# print(xy)
xz = {z: k for k, z in enumerate(sd[2])}
# print(xz)


grid = [[[0] * (len(sd[2])) for i in range(len(sd[1]))] for j in range(len(sd[0]))]
print(len(sd[0]), len(sd[1]), len(sd[2]))

for o, [nx, ny, nz] in r:
    for x in range(xm[nx[0]], xm[nx[1]]):
        for y in range(xy[ny[0]], xy[ny[1]]):
            for z in range(xz[nz[0]], xz[nz[1]]):
                grid[x][y][z] = o

n = 0
for x in range(len(grid)-1):
    for y in range(len(grid[x])-1):
        for z in range(len(grid[x][y])-1):
            if grid[x][y][z]:
                print(n)
                n += (sd[0][x+1] - sd[0][x]) * (sd[1][y+1] - sd[1][y]) * (sd[2][z+1] - sd[2][z])
print(n)



# on x=11..13,y=11..13,z=11..13
# off x=11..13,y=11..13,z=11..13

# on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10
# on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10




# p = []
# n = 0
#
#
# def switch(state, x, y, z):
#     o = []  # List of new overlaps
#     print(state, x, y, z)
#     if state == 1:
#         o.append([state, x, y, z])
#     for s, ox, oy, oz in p:
#         for nx, ny, nz, nx_, ny_, nz_ in [[x[i], y[j], z[k], x[not i], y[not j], z[not k]] for i in range(2) for j in range(2) for k in range(2)]:
#             if state == s:
#                 if state == 1:
#                     ns = not state
#                 if state == 0:
#                     break
#             if state != s:
#                 ns = state
#             if ox[0] <= nx <= ox[1] and oy[0] <= ny <= oy[1] and oz[0] <= nz <= oz[1]:
#                 co = [ns, [0, 0], [0, 0], [0, 0]]  # New overlap
#                 if (nx_ < ox[0] or nx_ > ox[1]) and (ny_ < oy[0] or ny_ > oy[1]) and (nz_ < oz[0] or nz_ > oz[1]):
#                     co[1][x.index(nx)] = nx
#                     co[1][not x.index(nx)] = ox[not x.index(nx)]
#                     co[2][y.index(ny)] = ny
#                     co[2][not y.index(ny)] = oy[not y.index(ny)]
#                     co[3][z.index(nz)] = nz
#                     co[3][not z.index(nz)] = oz[not z.index(nz)]
#                     o.append(co)
#                     break
#                 elif ox[0] < nx <= nx_ < ox[1] and oy[0] < ny <= ny_ < oy[1] and oz[0] < nz <= nz_ < oz[1]:
#                     o.append([ns, x, y, z])
#                     break
#                 elif nx == ox[0] and nx_ == ox[1] and ny == oy[0] and ny_ == oy[1] and nz == oz[0] and nz_ == oz[1]:
#                     o.append([ns, x, y, z])
#                     break
#             elif nx < ox[0] <= ox[1] < nx_ and ny < oy[0] <= oy[1] < ny_ and nz < oz[0] <= oz[1] < nz_:
#                 o.append([ns, ox, oy, oz])
#                 break
#
#     for overlap in o:
#         p.append(overlap)
#     global n
#     print(p)
#     for co in o:
#         print(co)
#         print(n)
#         n += (2 * co[0] - 1) * ((co[1][1] - co[1][0]) + 1) * ((co[2][1] - co[2][0]) + 1) * ((co[3][1] - co[3][0]) + 1)
#
#
# def change(state):
#     return state == 'on '
#
# while True:
#     # print(n)
#     s = input()
#     if s == '': break
#     state = change(s[:3])
#     s = s[3:]
#     if state == 0:
#         s = s[1:]
#     xyz = [[0, 0], [0, 0], [0, 0]]
#     for t in range(3):
#         s = s[2:]
#         for i in range(len(s)):
#             if s[i] == '.':
#                 xyz[t][0] = int(s[:i])
#                 s = s[i+2:]
#                 break
#         for i in range(len(s)):
#             if s[i] == ',':
#                 xyz[t][1] = int(s[:i])
#                 s = s[i+1:]
#                 break
#     xyz[2][1] = int(s)
#     # n +=
#     switch(state, xyz[0], xyz[1], xyz[2])
# print(n)
