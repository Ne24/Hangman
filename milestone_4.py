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
        #print(self.word_guessed) # shows inital length of word obfuscated with "_"
        self.word = self.word.lower()
        guess = guess.lower()

        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for index_no, y in enumerate(self.word,0): # using enumerate instead of a counter (no need to set count = 0 and increment at end of each iteration)
                if y == guess:
                    # guess.index(y) ## can't use because this runs into problems for words with common characters as it only returns the pos of the first char
                    self.word_guessed[index_no] = guess

            self.num_letters -=1
            print(self.word_guessed) # Shows word with correctly guessed letter positions revealed
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):

        while True:

                guess = input("Enter a single letter: ")

                if not(len(guess) == 1) and not(guess.isalpha()):
                    print("Invalid letter. Please, enter a single alphabetical character")

                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                    
                else:
                    self.check_guess(guess)
                    # self.list_of_guesses.append(guess)
                    self.list_of_guesses.insert(0, guess) # prepends guess to the list_of_guesses
                    break   
        return