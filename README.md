# Hangman

# Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

# milestone_2

## Description

Task concerns creating variables for the hangman game, a predefined list of four fruits is provided and printed. From this list, a random fruit is selected. The user provides the program with a character to guess (limited to one letter), if the guess exceeds one character an exception is raised, and the message: "Oops invalid input: More than one letter" is printed, If the guess is not a letter an exception is raised and the message: " Oops invalid input: This is not a letter" is printed, If no error is encountered, the while loop is broken and the program ends.

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
