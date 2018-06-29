#!python3

'''
Author: Andile Mbele
Date: 25 May 2018
Title: NumberGuesses.py
Credit: InventwithPython.com
'''

import random
import os
import sys

guessesTaken = 0

print("Hello!, what is your name player?")
#name = input()
name = sys.stdin.readline()


number = random.randint(1, 20)
print("Nice to meet you " + name + ", I'm thinking of a number between 1 and 20. Any idea what the number is?")

while guessesTaken < 6:
	print("Take a guess.")
	guess = input()
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
		print("Your guess is too low, Try again.")

		if guess > number:
			print("Your guess is too high, Try again.")

			if guess == number:
				break

if guess == number:
	guessesTaken = str(guessesTaken)
	print("Well done, " + name + ", you guessed my number in " + guessesTaken + " guesses!")
