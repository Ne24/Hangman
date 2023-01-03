
import random

word_list = ["Orange","Apple","Coconut", "Pear", "watermelon"]

print(word_list)

word = random.choice(word_list)

word = word.lower()

print(word)

    
def check_guess(guess):
    """Checks if guess input is in the word"""

    guess = guess.lower()

    if guess in word:
        print(f"Good guess {guess} is in the word!")
    else:
        print(f"Sorry {guess} is not in word. Try again.")


def ask_for_input():
    """Asks for guesss and check validity of guess """

    while True:

        try:
            guess = input("Enter a single letter: ")
            if len(guess) == 1 and guess.isalpha():
                pass
            elif len(guess) > 1:
                error_description = "Oops invalid input: More than one letter"    
                raise Exception()
            elif not(guess.isalpha()):
                error_description = " Oops invalid input: This is not a letter"   
                raise Exception() 
        except:
            print(error_description)
        else:
            break   
    check_guess(guess)


ask_for_input()


class Hangman():
    """"""
    import random

    def __init__(self, word_list, num_lives = 5 ) -> None:
        
        self.word = random.choice(self.word_list)
        self.word_guessed = []

        
        for x in self.word:
            self.word_guessed.append("_")
        
        # count =0 
        # #while num_lives >= 1:
        
        # for y in word:
        #     if guess == y:
        #         word_guessed[count] = guess
        #         count +=1
        #     else:
        #         # num_lives -=1
              

        self.num_letters = 0
        uniquecounter = 0

        for z in self.word:
            if uniquecounter > 0:
                if z not in word[:uniquecounter]:
                    self.num_letters +=1
            else:
                self.num_letters +=1 

            uniquecounter +=1

        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
    pass

    