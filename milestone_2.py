import random

word_list = ["Orange","Apple","Coconut", "Pear", "watermelon"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = ""



while len(guess) != 1 or not(guess.isalpha()):

    try:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess")
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
