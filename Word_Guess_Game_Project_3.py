"""Word_Guess_Game_Project_3
West C
This program is a two player secret word guessing game."""

import string # imports the Pythong strign module.

print ("This program is a two player secret word guessing game.")

# ask player one for a secret word

secret_word = input ("Player One, enter a secret word: ", ) .upper()
guessed_word = secret_word

# check for no puctuation and white space in the secret word. Use lecture info here
bad_chars = string.whitespace + string.punctuation # uses the Phyton string module to check for whitespace and punctuation

for char in secret_word: # from page 222 in the textbook
    if char in bad_chars: # remove the bad characters
        guessed_word = guessed_word.replace (char,'')


# print new lines so the secret word is not visible to Player Two.
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Player Two has the length of the word plus two more attempts.
num_guesses = len(secret_word) + 2

# main while loop of the game.
while num_guesses > 0:
    #print(f"Current guessed word: {guessed_word}")

# Ask Player Two for input and verify the accuracy of the input
    letter_guess = input ("Player Two, enter a letter you think is in the secret word:  ") .upper()


# Track the letters guessed and print the correct guesses

# Decrease the number of guesses remaining by one
else:
    num_guesses -= 1
    print ("Number of guesses remaining: ", num_guesses)

# Final guess to win the game
if guessed_word == secret_word:
    print("Congratulations, you have guessed the secret word {secret_word} !")
#    break

else:
    if guessed_word != secret_word:
        print ("Incorrect guess, the secret word was {secret_word}. Would you like to play again?")



z = input ("Pause, CWest")