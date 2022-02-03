syntax = []
characters = {']':'[', ')': '(', '}': '{', '>': '<'}
openingsymbols = ['(', '[', '{', '<']
points = {0: 1, 1: 2, 2: 3, 3: 4}
scores = []

while True:
    s = input()
    if s == '':
        break
    syntax.append(s)

def getscores(syntax):
    for line in syntax:
        score = 0
        store = []
        error = False
        for char in line:
            if char in openingsymbols:
                store.append(char)
            else:
                if store[len(store)-1] != characters[char]:
                    error = True
                    break
                else:
                    store.pop(len(store)-1)
        if not error:
            for i in range(len(store)):
                score *= 5
                score += points[openingsymbols.index(store[len(store)-1-i])]
            scores.append(int(score))

getscores(syntax)
scores.sort()
print(scores[int((len(scores)-1)/2)])