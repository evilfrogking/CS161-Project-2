"""Word_Guess_Game_Project_4
West C
This program is a two player secret word guessing game."""

import string # imports the Python string module.

print ("This program is a two player secret word guessing game.")

# ask player one for a secret word.
def ask_secret_word():
    """This is the function that will ask for a secret word from Player One."""
    while True:
        secret_word = input ("Player One, enter a secret word of only letters: ") .upper()
        # check that the secret word is a valid alphabetic word.
        if secret_word.isalpha(): #True / False Source: https://www.w3schools.com/python/ref_string_isalpha.asp
            # Remove punctuation and whitespace from secret word
            return "".join(char for char in secret_word if char.isalpha()) 
        return secret_word # this will capture the secret_word after the loop is doen so it can be used elsewhere.   ##### added

def display_guessed_word(guessed_word):
    """This is the function that will display the current guessed word."""
    # Display the current guessed_word.
    print (f"Current guessed word:  {guessed_word}")


def ask_letter_guess():
    """This is the function that will ask ask player Two for input and verify the accuracy."""
    # Ask Player Two for input and verify the accuracy of the input.
    while True:
        letter_guess = input ("Player Two, enter a letter you think is in the secret word:  ") .upper()
        # this will validate that the letter entered is a valid alphabetic entry and only one letter
        if letter_guess.isalpha() and len(letter_guess) ==1:
            return letter_guess
        else:
            print ("Please enter only one alphabetic letter: ")


def update_guessed_word (secret_word, guessed_word, letter_guess):
    """This is the function that will update the guessed word."""
    # If letter_guessed is in the secret word then update the guessed_word.
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
    # Show the new guessed word.
    return new_guessed_word

def main(secret_word):
    """Run all the helper functions of this program to play this word guessing game."""
    guessed_word = "*" * len(secret_word)
    guessed_letters = ""
    num_guesses = len(secret_word) + 2

# This is where I relied heavily on the lecture notes as a resource.
    while num_guesses > 0:
        display_guessed_word(guessed_word)
        letter_guess = ask_letter_guess()
        guessed_letters += letter_guess

        if letter_guess in secret_word:
            guessed_word = update_guessed_word(secret_word, guessed_word, letter_guess)
        else:
            # Decrease the number of guesses remaining by one.
            num_guesses -= 1
            print(f"Number of guesses remaining:  {num_guesses}")

        # Final guess to win the game.
        if guessed_word == secret_word:
            print(f"Congratulations, you have guessed the secret word {secret_word} !")
            break

    # If the final guess is incorrect .
    if guessed_word != secret_word:
        print (f"Incorrect guess, the secret word was:  {secret_word}. This game will end.")

secret_word = ask_secret_word()

# print new lines so the secret word is not visible to Player Two.
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# Call the main function.
main(secret_word)

z = input ("Pause, CWest")
