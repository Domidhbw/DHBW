import re
def printField(field):
    row = 0
    for x in field:
        if x == 'O':
            print('|O|',end="")
        elif x == 'I':
            print('|I|',end="")
        else:
            print("   ",end="")
        row += 1
        if row%3 == 0:
            print(' ')
            print('---------')

def takeAndCheckInput():
    pattern = re.compile(r'^(1|2|3),(1|2|3)$')
    pos = input('Its your turn player ' + playersTurn)
    if pattern.match(pos):
        print('nice ')
        print(pos)
        if field[translateInput(pos)] != 0:
            field[translateInput(pos)] = playersTurn
        else:
            print('try again')
            takeAndCheckInput()
    else:
        print('try again')
        takeAndCheckInput()

def translateInput(pos):
    if pos[0] == '1':
        return int(pos[2])-1
    elif pos[0] == '2':
        return 2+int(pos[2])
    elif pos[0] == '3':
        return 5+int(pos[2])

field = ["I",0,"O",
         "I","O",0,
         "I",0,0]

playersTurn = 'O'

print('Your goal is to be the first one to have 3 connectet chars')
print('You tell me where u wante to place your char by inputting y,x')
print('For example the second char in the first row would be presented by 1,2')

printField(field)

#having a game loop from here on

takeAndCheckInput()
#take player input
#validate it
#if correct
    #check for win
    #print it back 
#else start again from take player input
#change players turn to the other player and take player input