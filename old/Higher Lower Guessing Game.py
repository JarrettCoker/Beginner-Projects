# Higher Lower Guessing Game
# Python 3.5.1
# Written by Quadcor3

import random
name=input("Hello! What is your name?\n")
def guess_number():
    print("Well, {}, I am thinking of a number between 1 and 100.\nTake a guess.".format(name))
    number=random.randint(1, 100)
    z=0
    while True:
        deneme=int(input())
        deneme
        if deneme>number:
            print("Your guess is too high.")
            z=z+1
            continue
        elif deneme<number:
            print("Your guess is too low.")
            z=z+1
            continue
        else:
            z=z+1
            print("Good job, {}! You guessed my number in {} guesses!".format(name, z))
            break
guess_number()
while True:
    again=input("Do you wanna play again? y/n\n")
    if again=="y":
        guess_number()
    else:
        quit()
