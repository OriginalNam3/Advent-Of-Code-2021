# surprisingly simple, just arithmetic series stuff.
# not very neatly done, but it works.
# I don't want to work out the math for a general vy to stop the while loop at so I'm not going to :D

a = [[235, 259], [-118, -62]]

vxlst = []
for v in range(1, a[0][1]):  # Trying to do general solution, so have to find all vx such that (v*(v+1))/2 is in target area
    if a[0][0] <= (v * (v + 1)) / 2 <= a[0][1]:
        vxlst.append(v)

vx = max(vxlst)
vy = 0
while True:
    vy += 1
    py = 0
    s = 0
    while py > a[1][0]:
        py += vy - s
        if a[1][0] <= py <= a[1][1] and s >= vx - 1:
            print(vy)
            print(int((vy / 2) * (vy + 1)), '\n')
            break
        if py < a[1][1]:
            break
        s += 1
