platform = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
import random
i = 0


def showG():
    for i in platform:
        print(i)

def enemyP():
    ER = random.randint(0,2)
    EC = random.randint(0,2)
    if platform[r][c] != "O" or platform[r][c] != "X":
        platform[ER][EC] = "X"
    else:
        enemyP()

def winorlose():
    if platform[0][0] == platform[0][1] and platform[0][1] == platform[0][2]:
        i=10
        print(platform[0][0] + " Wins")
    elif platform[1][0] == platform[1][1] and platform[1][1] == platform[1][2]:
        i=10
        print(platform[0][0] + " Wins")
    elif platform[2][0] == platform[2][1] and platform[2][1] == platform[2][2]:
        i=10
        print(platform[0][0] + " Wins")
    elif platform[0][0] == platform[1][1] and platform[1][1] == platform[2][2]:
        i=10
        print(platform[0][0] + " Wins")
    elif platform[0][2] == platform[1][1] and platform[1][1] == platform[2][0]:
        i=10
        print(platform[0][0] + " Wins")



showG()

while i<9:
    r = int(input("What row: "))
    c = int(input("What collum: "))
    if platform[r][c] != "O" and platform[r][c] != "X":
        platform[r][c] = "O"
        enemyP()
        showG()
        i = i+1
    else:
        print("Another Number")
    winorlose()