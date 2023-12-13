import re
def printField(field):
    row = 0
    for x in field:
        if x == 0:
            print("   ",end="")
        else:
            print('|' + x + '|',end="")
        row += 1
        if row%3 == 0:
            print(' ')
            print('---------')

def takeAndCheckInput():
    pattern = re.compile(r'^(1|2|3),(1|2|3)$')
    print('Its your turn player ' + playersTurn)
    pos = input()
    if pattern.match(pos):
        if field[translateInput(pos)] == 0:
            field[translateInput(pos)] = playersTurn
        else:
            print('try again')
            takeAndCheckInput()
    else:
        print('try again')
        takeAndCheckInput()

def translateInput(pos):
    if pos[0] == '1':
        return (int(pos[2])-1)
    elif pos[0] == '2':
        return (2+int(pos[2]))
    elif pos[0] == '3':
        return (5+int(pos[2]))

def checkForWin():
    if checkForHorizontalWin():
        return True
    if checkForVerticalWin():
        return True
    if checkForQuer():
        return True
    
def checkForQuer():
    if field[0] == field[4] and field[0] == field[8] and field[0] != 0:
        return True
    if field[2] == field[4] and field[2] == field[6] and field[2] != 0:
        return True
    return False

def checkForVerticalWin():
    i = 0
    vertical = (0,1,2)
    for x in vertical:
        if field[x] != 0:
            if field[x] == field[x+3] and field[x] == field[x+6]:
                return True
        elif i == 2:
            return False
        i += 1

def checkForHorizontalWin():
    i = 0
    horizontal = (0,3,6)
    for x in horizontal:
            if field[x] != 0:
                if field[x] == field[x + 1] and field[x] == field[x + 2]:
                    return True
            elif i == 2:
                return False

def checkForDraw():
    for x in field:
        if x == 0:
            return False
    return True

field = [0,0,0,
         0,0,0,
         0,0,0]


playerOneChar = 'X'
playerTwoChar = 'O'
playersTurn = playerOneChar
gameNotFinished = True

print('Your goal is to be the first one to have 3 connectet chars')
print('You tell me where u wante to place your char by inputting y,x')
print('For example the second char in the first row would be presented by 1,2')

printField(field)

while(gameNotFinished):
    takeAndCheckInput()
    printField(field)
    if checkForWin():
        print('Congrats to '  + playersTurn + 'You Won')
        gameNotFinished = False
    if checkForDraw():
        print('You drawed')
        gameNotFinished = False
    if playersTurn == playerOneChar:
        playersTurn = playerTwoChar
    else:
        playersTurn = playerOneChar

#TODO add possibility to choose your player