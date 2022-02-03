gamma = ''
epsilon = ''
count = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
while True:
    s = str(input())
    if s == '':
        break
    for x in range(12):
        if s[x] == '1':
            count[x][1] += 1
        if s[x] == '0':
            count[x][0] += 1

for x in range(12):
    digit = str(count[x].index(max(count[x])))
    gamma = gamma + digit

for x in range(12):
    if gamma[x] == '0':
        epsilon = epsilon + '1'
    if gamma[x] == '1':
        epsilon = epsilon + '0'

print(int(gamma,2)*int(epsilon,2))