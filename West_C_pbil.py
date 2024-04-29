"""pbil_draft.py
Carrie West
This file will print pbil while the mispelled word alphebetical is enter by a user.
"""

#prompt the user to input the mispelled word.
user_input = str(input ("Please type in the work alphebetical: "))

#if the user inputs alphebetical correctly then print pbil.
while user_input == str("alphebetical"):
     print ("pbil !")
#prompt the user to again input the mispelled word.
     user_input = str(input ("Please type in the work alphebetical: "))

#if the user enters an incorrect word end the game.
else:
     print ("Incorrect, end of game.")

z = input ("end, CWest")
