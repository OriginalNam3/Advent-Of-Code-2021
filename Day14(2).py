# Probably didn't do it to the best of my ability, codes a bit messy

polymer = 'SHHNCOPHONHFBVNKCFFC'
rules = {}
pairs = {}
elements = {}

while True:
    s = input()
    if s == '':
        break
    rules[s[0:2]] = s[6]
    pairs[s[0:2]] = 0

for element in polymer:
    if element not in elements: elements[element] = 1
    else: elements[element] += 1
for i in range(len(polymer)-1):
    if polymer[i: i+2] in pairs: pairs[polymer[i:i + 2]] += 1


def pair_check(pair, n, dict):
    newpairs = dict.copy()
    for npair in [pair[0] + rules[pair], rules[pair] + pair[1]]:
        if npair in pairs:
            newpairs[npair] += n
    return newpairs


def insert():
    newpairs = pairs.copy()
    for pair in pairs:
        temp = pairs[pair]
        newpairs = pair_check(pair, temp, newpairs)
        newpairs[pair] -= temp
        if rules[pair] in elements: elements[rules[pair]] += temp
        else: elements[rules[pair]] = temp
    return newpairs

for x in range(40):
    pairs = insert()

print(elements)
element_count = list(elements[i] for i in elements)
print(element_count)
print(max(element_count) - min(element_count))