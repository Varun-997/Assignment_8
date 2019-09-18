import random
from itertools import combinations

def collinear(x1,y1,x2,y2,x3,y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
    if (a == 0): 
        return 1
    else: 
        return 0
def evaluate(str):
    collpnt = []
    comb = combinations(list(range(0,len(str))), 3)
    for i in list(comb):
        j= i[0]
        x1 = str[j] % 3
        y1 = str[j] // 3
        k = i[1]
        x2 = str[k] % 3
        y2 = str[k] // 3
        l = i[2]
        x3 = str[l] % 3
        y3 = str[l] // 3
        if collinear(x1,y1,x2,y2,x3,y3):
            collpnt.append(i)
    return collpnt



data = [0,0,0,0,0,0,0,0,0]
pos1 = []
pos2 = []
a = []
b = []
print("Welcome to the game")
y = random.randint(1,2)
o  = y
chan = 0
while 1:
    print("It is player",o,"'s chance")
    pos = int(input("Enter the position "))
    if pos > 8 or pos < 0:
        print('Enter valid Position between 0 to 8')
        continue
    no = int(input("Enter the number to be entered "))
    if no > 9 or no < 0:
        print('Enter valid no between 0 to 9')
        continue
    if (no % 2) == 0 and (chan % 2) == 0:
        print('Enter any odd no between 0 to 9')
        continue
    if (no % 2) != 0 and (chan % 2) != 0:
        print('Enter any even no between 0 to 9')
        continue
    data[pos] = no
    print(data[0:3])
    print(data[3:6])
    print(data[6:9])
    if (chan % 2) == 0:
        pos1.append(pos)
    if (chan % 2) != 0:
        pos2.append(pos)
    if len(pos1)>=3:
        a = evaluate(pos1)
    if len(pos2)>=3:
        b = evaluate(pos2)
    if(len(pos1)>=3):
        for k in a:
            if data[pos1[k[0]]] +  data[pos1[k[1]]] + data[pos1[k[2]]] >= 15:
                print("Player",y,"wins")
                exit()
    if(len(pos2)>=3):
        for l in b:
            if data[pos2[l[0]]] +  data[pos2[l[1]]] + data[pos2[l[2]]] >= 15:
                print("Player",y,"doesnt wins")
                exit()
    if chan == 8:
        print("Match Draw")
        exit()            
    chan+=1
    if o == 1:
        o = 2
    else:
        o = 1 
    print(pos1, pos2)
    
