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