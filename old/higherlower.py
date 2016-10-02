# Higher Lower Guessing Game
# Python 3.5.1
# Written by rsz

import random

def game():
    guesses = 0
    # assign a random number
    number = random.randint(1, 100)

    # main loop
    while True:
        n = int(input("Enter your guess: "))
        if n == number:
            guesses += 1
            print("You guessed correctly, the number was ", n)
            print("You took ", guesses," guesses ")

            choice = input("Play again? (y/n)").lower()
            if choice == "yes" or choice == "y":
                game()
            else:
                break

        elif n < number:
            print("Try higher Numbers\n")
        else:
            print("Try lower Numbers\n")

        guesses += 1

print("Welcome")
print("Try to guess the number")

game()
