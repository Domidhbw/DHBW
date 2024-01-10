def Pyramid(n):
    for x in range(n+1):
        print(str(x)*x)

import random

def Game():
    possibleActions = ['Rock', 'Paper', 'Scissors']
    computerAction = random.randint(1, 3)

    while True:
        try:
            userInput = int(input('Enter a choice ("1" for ' + possibleActions[0] + ', "2" for ' + possibleActions[1] + ' or "3" for ' + possibleActions[2] + '): '))
            if 1 <= userInput <= 3:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("That is not a valid option! Please enter a number.")

    print('You chose ' + possibleActions[userInput - 1])
    print('Computer chose ' + possibleActions[computerAction - 1])

    winner = determine_winner(userInput, computerAction)
    print(winner)

def determine_winner(user, computer):
    # Define winning conditions using a dictionary
    winning_conditions = {
        (1, 3): 'You win!',
        (2, 1): 'You win!',
        (3, 2): 'You win!',
        (1, 2): 'Computer wins!',
        (2, 3): 'Computer wins!',
        (3, 1): 'Computer wins!',
    }

    if user == computer:
        return 'It\'s a tie!'
    else:   
        return winning_conditions.get((user, computer), 'Invalid input!')
    
Game()