sorting = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6}
ref = {0: 'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g'}
check = [[6, 5, 5, 5, 6, 3, 7, 6], [6, 4, 5, 6, 7, 6], [6, 2, 5, 5, 4, 3, 7, 6], [5, 5, 4, 5, 6, 7, 6], [6, 5, 6, 7], [6, 2, 5, 4, 5, 6, 3, 7, 6], [6, 5, 5, 5, 6, 7, 6]]
symbols = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
total = 0

def sortalpha(s):
    news = ''
    for x in range(7):
        for c in s:
         if c == ref[x]:
             news += c
    return news

def sortnums(nums):
    newlst = []
    for n in range(1, 8):
        for num in nums:
            if num == n:
                newlst.append(num)
    return newlst


def mapping(lst):
    dict = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[]}
    for x in lst:
        for alpha in x:
            dict[alpha].append(len(x))
    newlst = []
    for x in dict:
        newlst.append(dict[x])
    return newlst

def actualinput(s, config):
    news = ''
    for c in s:
        news += ref[config.index(c)]
    return str(symbols.index(sortalpha(news)))


while True:
    output = []
    map = []
    config = ['', '', '', '', '', '', '']
    letters = [0, 0, 0, 0, 0, 0, 0]
    sort = ['', '', '', '']
    s = input()
    temp = ''
    delimiter = 0
    if s == '':
        break
    for i in range(len(s)):
        if s[i] == '|':
            delimiter = i
            break
    for char in s[0: delimiter]:
        if char.isalpha():
            temp += char
        if char.isspace():
            map.append(sortalpha(temp))
            temp = ''
    for char in s[delimiter+2:len(s)]:
        if char.isalpha():
            temp += char
        if char.isspace():
            output.append(sortalpha(temp))
            temp = ''
    output.append(temp)
    map = mapping(map)
    print(map)
    for x in range(7):
        for y in range(7):
            if sortnums(map[x]) == sortnums(check[y]):
                config[y] = ref[x]
    num = ''
    for digit in output:
        num += actualinput(digit, config)
    total += int(num)
    print(total)

# abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg | acdeg acdfg abdfg abdefg