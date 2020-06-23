# Write your code here
import random


class RockPaperScissors:
    options = ['rock', 'paper', 'scissors']
    # user_name = ''

    def __init__(self):
        self.user_name = input('Enter your name: ')
        self.user_rating = 0

        self.greet()
        self.ratings(self.user_name)
        self.play()

    def greet(self):
        print(f'Hello {self.user_name}')

    def ratings(self, user_name=''):
        ratings = open('./rating.txt', 'r+')
        if ratings.read().find(user_name) != 0:
            return ratings.close()

        for line in ratings:
            if line.find(user_name) != -1:
                # print(user_name)
                self.user_rating = int(line.split()[1].rstrip('\n'))
        ratings.close()

    def play(self):

        while True:
            pick = input()

            if pick == '!exit':
                print('Bye!')
                return False

            if pick == '!rating':
                print(f'Your rating: {self.user_rating}')
                continue

            if pick not in self.options:
                print('Invalid input')
                continue

            random.seed()
            computer = random.randint(0, 2)
            user = self.options.index(pick)

            if computer == user:
                print(f'There is a draw {self.options[user]}')
                self.user_rating += 50

            if computer - 1 == user or computer == user - 2:
                print(f'Sorry, but computer chose {self.options[computer]}')

            if computer + 1 == user or computer - 2 == user:
                print(f'Well done. Computer chose {self.options[computer]}')
                self.user_rating += 100


RockPaperScissors()
