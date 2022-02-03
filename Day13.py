paper = []
delimiter = 0

for j in range(895):
    row = []
    for i in range(1311):
        row.append(0)
    paper.append(row)

while True:
    s = input()
    if s == '': break
    templst = list(s)
    delimiter = templst.index(',')
    paper[int(s[delimiter + 1:len(s)])][int(s[0:delimiter])] = 1


def show():
    print(len(paper), len(paper[0]))
    for y in range(len(paper)):
        print(paper[y])
    print('\n')


def copy(x, y):
    newcopy = []
    for row in range(y):
        newrow = []
        for column in range(x):
            newrow.append(paper[row][column])
        newcopy.append(newrow)
    return newcopy


def foldx(x):
    global paper
    newpaper = copy(x, len(paper))
    for row in range(len(paper)):
        for column in range(x):
            if paper[row][len(paper[0]) - 1 - column] == 1:
                newpaper[row][column] = 1
    paper = newpaper


def foldy(y):
    global paper
    newpaper = copy(len(paper[0]), y)
    for row in range(y):
        for column in range(len(paper[0])):
            if paper[len(paper) - 1 - row][column] == 1:
                newpaper[row][column] = 1
    paper = newpaper


def countdots():
    count = 0
    for row in range(len(paper)):
        for column in range(len(paper[0])):
            if paper[row][column] == 1:
                count += 1
    return count


foldx(655)
foldy(447)
foldx(327)
foldy(223)
foldx(163)
foldy(111)
foldx(81)
foldy(55)
foldx(40)
foldy(27)
foldy(13)
foldy(6)
show()

# 1310, 893 is paper size (meaning there are 1311 columns and 894 rows with zero accounted for)
# KJBKEUBG
# [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0]
# [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
# [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
# [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
# [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
# [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
