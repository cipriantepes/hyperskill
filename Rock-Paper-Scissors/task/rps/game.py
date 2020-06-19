# Write your code here
options = ['rock', 'paper', 'scissors']


def play(pick):
    computer = 0
    if options.index(pick) < 2:
        computer = options.index(pick) + 1

    print(f'Sorry, but computer chose {options[computer]}')


play(input())
