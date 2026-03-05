
import random
choice = input('''Enter your Choice
             Rock
             Paper
             Scissor\n\t''')

choice1=choice.lower()

systemchoice = random.choice(['rock', 'paper', 'scissor'])


print(f"system choice is: {systemchoice}")


def winORloose():
    if (systemchoice == 'rock'):
        if (choice1 == 'paper'):
            print('WIN')
        elif (choice1 == 'rock'):
            print('DRAW')
        else:
            print('LOST')

    if (systemchoice == 'paper'):
        if (choice1 == 'scissor'):
            print('WIN')
        elif (choice1 == 'paper'):
            print('DRAW')
        else:
            print('LOST')

    if (systemchoice == 'scissor'):
        if (choice1 == 'rock'):
            print('WIN')
        elif (choice == 'scissor'):
            print('DRAW')
        else:
            print('LOST')


winORloose();

