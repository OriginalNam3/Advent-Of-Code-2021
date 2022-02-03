caves = []
connections = []
global paths
paths = 0

# this input sucks, half of the code is just dealing with the input >:(
# Also probably doesn't help that I'm copy and pasting it in and I'm not exactly an expert, but hey, I can practice using slices :D
while True:
    s = input()
    if s == '':
        break
    delimiter = 0
    for x in range(len(s)):
        if s[x] == '-': break
    delimiter = x
    if s[:delimiter] in caves:
        connections[caves.index(s[:delimiter])].append(s[delimiter + 1:])
    else:
        caves.append(s[:delimiter])
        connections.append([s[delimiter+1:]])
    if s[delimiter+1:] in caves:
        connections[caves.index(s[delimiter+1:])].append(s[:delimiter])
    else:
        caves.append(s[delimiter+1:])
        connections.append([s[:delimiter]])

def pathing(cave, travelled, doubled):
    global paths
    ntravelled = travelled.copy()
    if cave[0].islower():
        ntravelled.append(cave)
    if cave == 'end':
        paths += 1
        return
    for adjcave in connections[caves.index(cave)]:
        if not doubled and adjcave != 'start' and adjcave in ntravelled:
            pathing(adjcave, ntravelled, True)
        if not doubled and adjcave != 'start' and adjcave not in ntravelled:
            pathing(adjcave, ntravelled, False)
        if doubled and adjcave not in ntravelled:
            pathing(adjcave, ntravelled, True)

pathing('start', [], False)
print(paths)