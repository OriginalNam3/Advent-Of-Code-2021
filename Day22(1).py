# This was okay. I found out this weird thing where if u have:
# grid = [[0]*10]*10
# If you then do something like grid[1][1] = 2, it changes the all elements with index 1. Idk if it's a bug or what.
# Learned a great trick of adding all elements in muiltidimensional list to one list and then summing (while the list are bool integers)
# to see how many are true. That is quite a good and neat mechanic and you can do it in one line with a couple for statements.

grid = [[[0 for a in range(101)] for b in range(101)] for c in range(101)]


def switch(state, x, y, z, grid):
    print(x, y, z)
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            for k in range(z[0], z[1]+1):
                grid[i+50][j+50][k+50] = state
    return grid


def change(state):
    return state == 'on '


def count(grid):
    ng = [grid[x][y][z] for x in range(len(grid)) for y in range(len(grid[x])) for z in range(len(grid[x][y]))]
    return sum(ng)


while True:
    s = input()
    state = change(s[:3])
    s = s[3:]
    if state == 0:
        s = s[1:]
    xyz = [[0, 0], [0, 0], [0, 0]]
    for t in range(3):
        s = s[2:]
        for i in range(len(s)):
            if s[i] == '.':
                xyz[t][0] = int(s[:i])
                s = s[i+2:]
                break
        for i in range(len(s)):
            if s[i] == ',':
                xyz[t][1] = int(s[:i])
                s = s[i+1:]
                break
    xyz[2][1] = int(s)
    grid = switch(state, xyz[0], xyz[1], xyz[2], grid)
    print(count(grid))

# My puzzle input:
# on x=-40..6,y=-36..9,z=-36..12
# on x=-22..31,y=-48..6,z=-35..9
# on x=3..47,y=-13..37,z=-14..36
# on x=-27..22,y=-34..19,z=-49..2
# on x=-14..37,y=-31..23,z=-19..33
# on x=-3..41,y=-9..37,z=-43..8
# on x=-41..4,y=-26..18,z=-26..27
# on x=-15..32,y=-48..4,z=-34..19
# on x=-31..13,y=-12..36,z=-45..8
# on x=-20..31,y=-36..16,z=-22..26
# off x=-49..-33,y=13..31,z=3..15
# on x=-29..17,y=-49..0,z=-19..25
# off x=30..47,y=24..39,z=-29..-18
# on x=4..49,y=-47..7,z=-24..23
# off x=-29..-15,y=9..19,z=-20..-11
# on x=-24..27,y=-18..27,z=-8..42
# off x=-18..-7,y=-39..-24,z=7..24
# on x=-48..6,y=-35..15,z=-21..29
# off x=-2..16,y=-12..2,z=-7..9
# on x=-39..8,y=-7..44,z=-33..14


# on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10
# on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10