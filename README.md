# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Description

Task concerns creating variables for the hangman game, a predefined list of four fruits is provided and printed. From this list, a random fruit is selected. The user provides the program with a character to guess (limited to one letter), if the guess exceeds one character an exception is raised, and the message: "Oops invalid input: More than one letter" is printed, If the guess is not a letter an exception is raised and the message: " Oops invalid input: This is not a letter" is printed, If no error is encountered, the while loop is broken and the program ends.
## milestone_2



# milestone 3

Two functions added:

1. check_guess

The guess provided by user is passed to the check_guess function, where it is converted to lowercase, then the selected word is checked to see if it contains the guess.


2. ask_for_input

This function iteratively asks the user for valid input, and raises an error if input is invalid.
Currently it checks:

1. length
2. entry is a letter 

If input is valid, the loop is broken and the value of guess passed to the check_guess function.

# milestone 4

The class Hangman utilises object oriented programming to play a game.
When an instance of Hangman is created, a word_list and number_of_lives (default value = 5) are initiated.
within the __init__ method many attributes are initalised including:

word
word_guessed
list_of_guesses
num_letters
uniquecounter

There are two additional methods of Hangman that are vital for the game's functionality:

1. *check_guess*, this takes the random word selection choosen by the random module and lowers the case, this is also done for the guess entered by the user, thus all letters are in lower case. It then checks if the guess is persent in the word, if it is, the user is notified and the position of the character is revealed within the word, unguessed words remain hidden. the *number_of_letters* is reduced by one. If the guess is incorrect the user is notified of the incorrect choice and the reduction of *num_lives* by 1

2. *ask_for_input*, prompts the user to enter a guess that is a letter and is not more than one letter, if the guess has been made previously, the user will be reminded this guess has been already made. If the guess adheres to the requirements, it is deemed valid and is passed into the *check_guess* method.
This guess is prepended to the *list_of_guesses* list. 