# Hangman game
# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
from random import choice
import re


def main():
    print("Welcome in Hangman. Let's play!")
    rep = True

    while rep:
        # Play one tally
        game()

        # Ask player if they want to repeat game
        rep = repeat()


# Read dictionary into memory
def prepare_dict():
    # Create an empty list
    dictionary = []

    # Read words from the dictionary to the list
    with open("sowpods.txt", 'r') as dict_txt:
        while True:
            line = dict_txt.readline()

            if not line:
                break

            line = line.strip()
            dictionary += [line]

    return dictionary


# Generate random word
def rand_word(dictionary):
    return choice(dictionary)


# One tally of game
def game():
    # Load a dictionary to choose word from
    dictionary = prepare_dict()

    # Word to guess
    word = rand_word(dictionary)

    # List to keep track of letters, the player tried to guess and correct letters
    letters = []
    in_word = []
    correct = 0
    mistakes = 0

    # Instruct the user
    print("Guess a word, letter by letter.")
    print_letters(word, in_word)

    while True:
        # Get player's guess
        letter = guess()

        # Player repeated guessed letter
        if letter in letters:
            print("You've already tried that.")

        # Player entered a new letter
        else:
            letters += [letter]

            # Player guessed correctly
            if check(word, letter):
                in_word += [letter]
                correct = print_letters(word, in_word)

            # Player guessed wrong
            else:
                mistakes += 1
                if mistakes < 5:
                    print(f"You've got {6 - mistakes} incorrect guesses left.")
                elif mistakes == 5:
                    print(f"You've got only one incorrect guess left.")

            # Quit when all letters are guessed
            if correct == len(word):
                print("Congratulations!")
                break

            # Or quit when player made too many mistakes
            elif mistakes == 6:
                print(f"You failed, the word was {word}. Good luck next time!")
                break


# Get player's guess
def guess():
    while True:
        letter = input("Guess your letter: ")

        # Correct input
        if letter.isalpha() and len(letter) == 1:
            return letter.upper()

        # Incorrect input
        else:
            print("Incorrect input. You need to enter one letter")


# Check if the letter is in the word
def check(word, letter):

    # Player guessed correctly
    if letter in word:
        return True

    # Player guessed wrong
    else:
        print("Nope.")
        return False


# Print words or underscores
def print_letters(word, letters):
    # Keep track of how many letters are guessed
    correct = 0

    for letter in word:

        # Print guessed letters
        if letter in letters:
            print(letter, end=' ')
            correct += 1

        # Print underscores for not guessed letters
        else:
            print("_", end=' ')

    print()
    return correct


# Check if players want to play again
def repeat():
    again = input("Do you want to play again? (y/n)")
    while True:
        if re.search("y(es)?", again, re.IGNORECASE):
            print("Let's start then!")
            return True
        elif re.search("n(o)?", again, re.IGNORECASE):
            print("Ok, bye!.")
            return False
        else:
            print("Incorrect answer.")
            again = input("Make up your mind... : ")


if __name__ == '__main__':
    main()
