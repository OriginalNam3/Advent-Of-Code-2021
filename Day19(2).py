# Not much different to part 1


def getd(o, t):
    return ((o[0]-t[0])**2)+((o[1]-t[1])**2)+((o[2]-t[2])**2)


def findcommon(od, td):
    ci = []
    for i in range(len(od)):
        for j in range(len(td)):
            if od[i] == td[j]:
                ci.append(i)
    return ci


def findo(oc, rc):
    v = [oc[1][i] - oc[0][i] for i in range(3)]
    u = [rc[1][i] - rc[0][i] for i in range(3)]
    o = []
    for i in range(3):
        for j in range(3):
            for k in [-1, 1]:
                if v[i] == u[j]*k:
                    o.append([j, k])
    return o


def getmd(o, t):
    return abs(o[0]-t[0])+abs(o[1]-t[1])+abs(o[2]-t[2])

c = []
scanners = []
spos = []


s = input()
while True:
    s = input()
    if s == '': break
    c.append(list(map(int, s.split(','))))

d = [[getd(b, b_) for b_ in c] for b in c]

while True:
    s = input()
    if s == '': break
    ncoords = []
    while True:
        s = input()
        if s == '': break
        ncoords.append(list(map(int, s.split(','))))
    scanners.append(ncoords)

while scanners:
    print(len(scanners))
    for x in range(len(scanners)):
        ncoords = scanners[x]
        o = []
        for i in range(len(d)):
            for nc in ncoords:
                nd = [getd(nc, oc) for oc in ncoords]
                if len(findcommon(d[i], nd)) > 10:
                    o.append([c[i][:], nc[:]])
        if len(o) > 11:
            co = findo([o[2][0], o[3][0]], [o[2][1], o[3][1]])
            for i, [_, nc] in enumerate(o[:2]):
                o[i][1][:] = [nc[j] * k for j, k in co]
            pos = [o[0][0][i] - o[0][1][i] for i in range(3)]
            print(pos)
            spos.append(pos)
            dextension = []
            ncoords[:] = [[nc[j] * k for j, k in co] for nc in ncoords]
            ncoords[:] = [[nc[i] + pos[i] for i in range(3)] for nc in ncoords]
            ncoords_ = []
            for nc in ncoords:
                if nc not in c:
                    ncoords_.append(nc[:])
            ncoords[:] = ncoords_[:]
            for i in range(len(c)):
                for nc in ncoords:
                    d[i].append(getd(c[i], nc))
            c += ncoords_
            dextension = [[getd(nc, c_) for c_ in c] for nc in ncoords]
            d += dextension
            scanners.remove(ncoords)
            break
m = []
nspos = spos[:]
for x in spos:
    nspos.remove(x)
    for y in spos:
        m.append(getmd(x, y))
print(max(m))


# Output: (number of scanners left, detected position of new scanner)
# 25
# [-34, -39, -1212]
# 24
# [1276, -97, -1275]
# 23
# [-23, -18, 1148]
# 22
# [-16, 29, 2262]
# 21
# [-1232, 18, -1286]
# 20
# [-2296, -97, -1318]
# 19
# [-1152, 1250, -1236]
# 18
# [-2361, 82, -2400]
# 17
# [-2394, 32, -3766]
# 16
# [-1185, -91, -2525]
# 15
# [-2457, -48, -4796]
# 14
# [-2413, -1237, -3623]
# 13
# [-2354, 1125, -3678]
# 12
# [-2424, -1251, -1267]
# 11
# [-1164, -1250, 15]
# 10
# [-3490, -1240, -1188]
# 9
# [-2426, 1264, -2514]
# 8
# [-2341, 1264, -1211]
# 7
# [-2307, -2338, -1261]
# 6
# [-2316, -2427, 3]
# 5
# [-3651, -2454, 15]
# 4
# [-3533, -3667, -159]
# 3
# [-3623, 9, -3737]
# 2
# [-3477, 1147, -2567]
# 1
# [-2306, -1164, 24]
# Number of beacons: 330
# Maximum Manhattan distance: 9634
