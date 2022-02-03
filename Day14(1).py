polymer = 'SHHNCOPHONHFBVNKCFFC'
# polymer = 'NNCB'
rules = {}
while True:
    s = input()
    if s == '':
        break
    rules[s[0:2]] = s[6]

def findlocations():
    locations = []
    for i in range(len(polymer)-1):
        if polymer[i:i+2] in rules:
            locations.append([i, rules[polymer[i:i+2]]])
    return locations

def insert(locations): #locations being [[index, element to insert], [index, element to insert]]
    newpolymer = ''
    for i in range(len(polymer)):
        newpolymer += (polymer[i])
        for lst in locations:
            if i == lst[0]:
                newpolymer += (lst[1])
    return newpolymer

def countelements():
    elements = []
    count = []
    for i in polymer:
        if i not in elements:
            elements.append(i)
            count.append(1)
        else:
            count[elements.index(i)] += 1
    return (max(count)- min(count))

for x in range(10):
    newlocations = findlocations()
    polymer = insert(newlocations)
print(countelements())

