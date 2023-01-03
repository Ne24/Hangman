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