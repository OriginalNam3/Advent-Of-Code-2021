hlines = []
vlines = []
dlines = []
ulines = []
graph = []
count = 0
for x in range(1000):
    row = []
    for y in range(1000):
        row.append(0)
    graph.append(row)
while True:
    s = input()
    a = []
    b = []
    if s == '':
        break
    for c in range(len(s)-1):
        if s[c] == ' ' and s[c+1] == '-':
            for x in range(len(s[0:c])):
                if s[0:c][x] == ',':
                    a.append(int(s[0:c][0:x]))
                    a.append(int(s[0:c][x+1:len(s[0:c])]))
        if s[c+1] == ' ' and s[c] == '>':
            for x in range(len(s[c+2:len(s)])):
                if s[c+2:len(s)][x] == ',':
                    b.append(int(s[c+2:len(s)][0:x]))
                    b.append(int(s[c+2:len(s)][x+1:len(s[c+2:len(s)])]))
    if a[0] == b[0]:
        vlines.append([a, b])
    if a[1] == b[1]:
        hlines.append([a, b])
    if (a[1] < b[1] and a[0] < b[0]) or (b[1] < a[1] and b[0] < a[0]):
        ulines. append([a, b])
    if (a[1] < b[1] and a[0] > b[0]) or (a[1] > b[1] and a[0] < b[0]):
        dlines.append([a, b])


for vline in vlines:
    for y in range(abs(vline[0][1]-vline[1][1])+1):
        graph[y + min([vline[0][1], vline [1][1]])][vline[0][0]] +=1
for hline in hlines:
    for x in range(abs(hline[0][0]-hline[1][0])+1):
        graph[hline[0][1]][x + min([hline[0][0], hline[1][0]])] += 1
for uline in ulines:
    for x in range(abs(uline[0][0]-uline[1][0])+1):
        graph[min([uline[0][1], uline[1][1]])+x][min([uline[0][0], uline[1][0]])+x] +=1
for dline in dlines:
    for x in range(abs(dline[0][0]-dline[1][0])+1):
        graph[max([dline[0][1], dline[1][1]])-x][min([dline[0][0], dline[1][0]])+x] +=1
for x in range(1000):
    print(graph[x])

for x in range(1000):
    for y in range(1000):
        if graph[y][x] > 1:
            count +=1
print(count)