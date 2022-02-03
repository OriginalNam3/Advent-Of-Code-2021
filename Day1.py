temp1 = int(input())
increased = 0
while True:
    temp2 = int(input())
    if temp2 > temp1:
        increased +=1
    temp1 = temp2
    print(increased)