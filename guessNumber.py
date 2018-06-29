#!python

#This is a guess the number game.

import random
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

#Ask the user to guess the number about 6 times.

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Too low, go up.')
    elif guess > secretNumber:
        print('Guess too high, go low.')
    else:
        break         #Correct condition guess!

if guess == secretNumber:
    print('Well Done! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I had in mind was ' + str(secretNumber))
