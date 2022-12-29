import random

word_list = ["Orange","Apple","Coconut", "Pear", "watermelon"]

print(word_list)

word = random.choice(word_list)

print(word)

try:

    guess = input("Enter a single letter: ")
    if len(guess) == 1:
        pass
    elif len(guess) > 1:    
        raise Exception()
except:
    print("This is more than one letter")

    
