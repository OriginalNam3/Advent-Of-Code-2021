# First part was easy.

count = 0
n = 0


def roll():
    global count
    count += 1
    global n
    n = (n % 100) + 1
    return n


p1s = 0
p2s = 0
p = [6, 8]

while True:
    p[0] = ((p[0] + roll() + roll() + roll() - 1) % 10) + 1
    p1s += p[0]
    if p1s >= 1000:
        print(count * p2s)
        break
    p[1] = ((p[1] + roll() + roll() + roll() - 1) % 10) + 1
    p2s += p[1]
    if p2s >= 1000:
        print(count * p1s)
        break
