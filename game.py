
import random
choice = input('''Enter your Choice
             Rock
             Paper
             Scissor\n\t''')
choice.lower()

systemchoice = random.choice(['rock', 'paper', 'scissor'])


print(f"system choice is: {systemchoice}")


def winORloose():
    if (systemchoice == 'rock'):
        if (choice == 'paper'):
            print('WIN')
        elif (choice == 'rock'):
            print('DRAW')
        else:
            print('LOST')

    if (systemchoice == 'paper'):
        if (choice == 'scissor'):
            print('WIN')
        elif (choice == 'paper'):
            print('DRAW')
        else:
            print('LOST')

    if (systemchoice == 'scissor'):
        if (choice == 'rock'):
            print('WIN')
        elif (choice == 'scissor'):
            print('DRAW')
        else:
            print('LOST')


winORloose();

