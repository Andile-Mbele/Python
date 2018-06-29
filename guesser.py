#!python3
'''
Guesser.py, by Andile Mbele, 2017-10-06
This program has the user guess a number between 1 to 100.
'''
import random

#def main():
    # Initialise the program 
print("Guess a number between 1 and 100.")    
    #randomNumber = 35 for debugging purposes only
randomNumber = random.randint(1,100)
found = False      # flag variable to see
                   # if they guessed it 
    # Run through the guessing process
while not found:
    userGuess = int(input("Your Guess:"))
    
    if userGuess == randomNumber:
       print("You Got It")
       found = True
    elif userGuess > randomNumber: 
         print("Guess lower!")
         
    else:
         print("Guess higher!")

         
print("Thank you for playing our game, we appreciate it.")
    
      
