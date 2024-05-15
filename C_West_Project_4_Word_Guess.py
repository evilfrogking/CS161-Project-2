"""Word_Guess_Game_Project_4
West C
This program is a two player secret word guessing game."""

import string # imports the Python string module.

print ("This program is a two player secret word guessing game.")

# ask player one for a secret word.
while True:
    secret_word = input ("Player One, enter a secret word of only letters: ") .upper()
    # check that the secret word is a valid alphabetic word.
    if secret_word.isalpha(): #True / False Source: https://www.w3schools.com/python/ref_string_isalpha.asp
        break

# Remove punctuation and whitespace from the secret word.
secret_word = ''.join(char for char in secret_word if char.isalpha())

# print new lines so the secret word is not visible to Player Two.
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Start an empty string for the guessed_word.
guessed_word = "*" * len(secret_word) 
# Start a string of letters guessed by player two.
guessed_letters = "" 
# Player Two has the length of the word plus two more attempts.
num_guesses = len(secret_word) + 2


# main while loop of the game.
while num_guesses > 0:
    # Display the current guessed_word.
    print (f"Current guessed word:  {guessed_word}")

    # Ask Player Two for input and verify the accuracy of the input.
    letter_guess = input ("Player Two, enter a letter you think is in the secret word:  ") .upper()

    # this will validate that the letter entered is a valid alphabetic entry and only one letter
    #letter_guess. isalpha()
    if not letter_guess.isalpha() or len(letter_guess) !=1:
        print ("Please enter only one alphabetic letter: ")
        continue

    # Track the letters guessed and print the correct guesses.
    guessed_letters += letter_guess

    # If letter_guessed is in the secret word.
    if letter_guess in secret_word:
        # Then update the guessed_word.
        new_guessed_word = ""
        # Iterate over the secret word.
        for index, letter in enumerate(secret_word):  # enumerate.
            # On each iteration: 
            # If the guessed letter equals to the letter in the secret word at the current index.
            if letter_guess == letter:
                # concatenate the letter to the guessed word.
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[index]

        # Update the guessed_word.
        guessed_word = new_guessed_word

    # Decrease the number of guesses remaining by one.
    else:
        num_guesses -= 1
        print(f"Number of guesses remaining:  {num_guesses}")

    # Final guess to win the game.
    if guessed_word == secret_word:
        print(f"Congratulations, you have guessed the secret word {secret_word} !")
        break

# If the final guess is incorrect .
if guessed_word != secret_word:
    print (f"Incorrect guess, the secret word was:  {secret_word}. This game will end.")


z = input ("Pause, CWest")