import random
class Hangman():
    """"""
    def __init__(self, word_list, num_lives = 5 ) -> None:

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.list_of_guesses = []
        self.num_letters = 0
        uniquecounter = 0
        
        for x in self.word:
            self.word_guessed.append("_")

        for z in self.word:
            if uniquecounter > 0:
                if z not in self.word[:uniquecounter]:
                    self.num_letters +=1
            else:
                self.num_letters +=1 

            uniquecounter +=1        
    pass   


    def check_guess(self,guess):
        """This function checks if the guess provided is in the word"""

        guess = guess.lower()

        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
        # else:
        #     print(f"Sorry {guess} is not in word. Try again.")            

    def ask_for_input(self):

        while True:

            try:
                guess = input("Enter a single letter: ")
                if not(len(guess) == 1) and not(guess.isalpha()):
                    print("Invalid letter. Please, enter a single alphabetical character")
                    error_description = "Oops invalid input: Not a single alphabetical character "    
                    raise Exception()
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                elif len(guess) > 1:
                    error_description = "Oops invalid input: More than one letter"    
                    raise Exception()
                elif not(guess.isalpha()):
                    error_description = " Oops invalid input: This is not a letter"   
                    raise Exception() 
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                    # self.list_of_guesses.append(guess)
                    # self.list_of_guesses.insert(0, guess) # prepends guess to the list_of_guesses
            except:
                print(error_description)
            else:
                break   
        # self.list_of_guesses.append(guess)
        # return self.list_of_guesses


Hangman.ask_for_input()