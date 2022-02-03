# Lmao just had to change the format a bit to lower runtime but I didn't do much different.

alg = input()
alg = [char == '#' for char in alg]
s = input()


grid = []
while True:
    s =input()
    if s == '':
        break
    grid.append(s)

image = [[0] * 10 + [char == '#' for char in row] + [0] * 10 for row in grid]
for _ in range(10):
    image.append([0] * len(image[0]))
    image.insert(0, [0] * len(image[0]))


def count(image):
    nimage = image[10:-10]
    nimage = [row[10:-10] for row in nimage]
    return sum(map(sum, nimage))


def enhance(image):
    oimage = []
    for row in image:
        oimage.append([0] * 10 + row + [0] * 10)
    for _ in range(10):
        oimage.insert(0, [0] * (len(image[0])+20))
        oimage.append([0] * (len(image[0])+20))
    nimage = [[0] * (len(oimage[row])-2) for row in range(len(oimage) - 2)]
    for x in range(1, len(oimage)-1):
        for y in range(1, len(oimage[0])-1):
            n = [oimage[nx][ny] for nx in [x-1, x, x+1] for ny in [y-1, y, y+1]]
            nimage[x-1][y-1] = alg[int(''.join(map(str, map(int, n))), 2)]
    return nimage


for _ in range(25):
    for _ in range(2):
        image = enhance(image)
    image = image[10:-10]
    image = [row[10:-10] for row in image]
    print(count(image))