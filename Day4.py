boards = []
marks = []
nums = []
winners = []
placement = 0

def check(n):
    for x in range(len(boards)):
        for row in range(5):
            for column in range(5):
                if boards[x][row][column] == n:
                    marks[x][row][column] = 1

def bingo(n):
    bingo = []
    for x in range(len(boards)):
        if not winners[x]:
            for a in range(5):
                rowcheck = 0
                colcheck = 0
                for b in range(5):
                    if marks[x][a][b] == 1:
                        rowcheck += 1
                    if marks[x][b][a] == 1:
                        colcheck += 1
                if rowcheck == 5:
                    print('Board ' + str(x) + ' has won on a row!')
                    score(x, n)
                    winners[x] = True
                if colcheck == 5:
                    print('Board ' + str(x) + 'has won on a column!')
                    score(x, n)
                    winners[x] = True

def score(x, n):
    total = 0
    for a in range(5):
        for b in range(5):
            if marks[x][a][b] == 0:
                total += boards[x][a][b]
    total *= n
    print('Board ' + str(x) + ' had a score of ' + str(total) + '!')


s = input()
temp = ''
for char in s:
    if char.isdigit():
        temp += char
    if char == ',':
        nums.append(int(temp))
        temp = ''
nums.append(temp)
s = input()

for t in range(99):
    board = []
    for x in range(5):
        count = 0
        row = []
        s = input()
        temp = ''
        for char in s:
            if char.isdigit():
                temp += char
            if char == ' ' and temp.isdigit():
                row.append(int(temp))
                temp = ''
        row.append(int(temp))
        board.append(row)
    boards.append(board)
    marks.append([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])
    winners.append(False)
    s = input()

for n in nums:
    check(n)
    bingo(n)