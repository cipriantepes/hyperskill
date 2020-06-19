# Write your code here
import random
options = ['rock', 'paper', 'scissors']


def play():

    while True:
        pick = input()

        if pick == '!exit':
            print('Bye!')
            return False

        if pick not in options:
            print('Invalid input')
            continue

        random.seed()
        computer = random.randint(0, 2)
        user = options.index(pick)

        if computer == user:
            print(f'There is a draw {options[user]}')

        if computer - 1 == user or computer == user - 2:
            print(f'Sorry, but computer chose {options[computer]}')

        if computer + 1 == user or computer - 2 == user:
            print(f'Well done. Computer chose {options[computer]}')

play()
