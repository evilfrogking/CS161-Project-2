"""GuessNumber.py
Carrie West
This program will prompt the user to guess a number between 0 and 100.
"""

import random #get the random number module.
number = random.randint(0,100) # get a random number between 0 and 100.

print("Guess a number between 0 and 100 inclusive.") # Introduc the user to the game.
print()

# get an initial guess
guess_str = input ("Guess a number: ")
guess = int(guess_str) # convert users input string to a number

# while the guess is within the range, keep asking
while 0 <= guess <= 100:
    if guess > number:
        print ("Too High.")
    elif guess < number:
        print ("Too Low.")
    else: # correct guess, exit with break
        print ("Just Right.  The answer was ", number)
        break
    # the loop keeps going, getting the next guess
    guess_str = input ("Guess a number: ")
    guess = int(guess_str)

z = input ("end, CWest")