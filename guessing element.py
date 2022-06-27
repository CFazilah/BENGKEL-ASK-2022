#!/usr/bin/env python

import random
from xml.dom.minidom import Element

def main():
    """Start a chemistry guessing game."""
    print("Guess the elements!")

    chemistryElement = [
        "iodin",
        "hidrogen",
        "magnesium",
        "calium",
        "natrium",
        ]

    x = random.choice(chemistryElement)
 
    guess = None

    while x != guess:

        guess = str(input("What element am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()


