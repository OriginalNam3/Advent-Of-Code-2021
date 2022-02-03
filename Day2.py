depth = 0
aim = 0
pos = 0
while True:
    s = input()
    if s[0:7] == 'forward':
        pos += int(s[8])
        depth += aim*int(s[8])
    if s[0:2] == 'up':
        aim -= int(s[3])
    if s[0:4] == 'down':
        aim += int(s[5])
    print(depth)
    print(pos)