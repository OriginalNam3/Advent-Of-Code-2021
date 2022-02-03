syntax = []
characters = {']':'[', ')': '(', '}': '{', '>': '<'}
symbols = [')', ']', '}', '>']
points = {0: 3, 1: 57, 2: 1197, 3: 25137}
count = [0, 0, 0, 0]
total = 0

while True:
    s = input()
    if s == '':
        break
    syntax.append(s)

for line in syntax:
    store = []
    for char in line:
        if char in ['[', '(', '{', '<']:
            store.append(char)
        if char in symbols:
            if store[len(store)-1] != characters[char]:
                count[symbols.index(char)] += 1
                break
            elif store[len(store)-1] == characters[char]:
                store.pop(len(store)-1)

for x in range(4):
    total += count[x]*points[x]

print(total)
