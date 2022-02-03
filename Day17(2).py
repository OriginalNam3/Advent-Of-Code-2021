# Spent half an hour debugging and found out it was a break statement I forgot in one of the if statements.  T.T

# Again, pretty easy but messed up a few times because of stuff like:
# vx that stay in range no matter the steps (vx such that ((vx/2) * (vx+1)) is within target area)
# Just index mistakes with the target area list and silly sign errors

# I think this is pretty much a perfect solution? I can narrow down the vx range but that's boring.
# It'd just be something like (2*targetarea)/(vx*(vx+1)) by rearranging the sequence.

a = [[235, 259], [-118, -62]]

vlst = []
for vx in range(1, a[0][1]+1):
    for vy in range(a[1][0], 118):
        p = [0, 0]
        s = 0
        while p[0] <= a[0][1] and p[1] >= a[1][0]:
            if vx-s > 0: p[0] += vx-s
            p[1] += vy-s
            if a[1][0] <= p[1] <= a[1][1] and a[0][0] <= p[0] <= a[0][1]:
                if [vx, vy] not in vlst:
                    vlst.append([vx, vy])
            s += 1

print(len(vlst))