# Higher Lower Guessing Game
# Python 2.7.10
# Written by Oddjob922

import random
import time
from types import *
import sys

def goagain():
	print "\nWould you like to play again? [Y/N]"
	opt = raw_input("\n>")
	if opt == 'Y' or opt == 'y':
		print """Welcome to Toz's 'Guess my number' Game!

To Play, please select a game option by typing the number 

of the option you would like to select:

1) Easy (1-50)
2) Medium (1-200)
3) Hard (1-500)
4) Custom
"""
		main()
	elif opt == 'N' or opt == 'n':
		print "\nThanks for playing!"
		sys.exit()
	else:
		print "\nThat is not a valid option!"
		goagain()


def guessEval(guessCountOrig, randStart, randEnd):
	num = random.randrange(randStart, randEnd)
	print "Okay, my number is between %r and %r!\n" % (randStart, randEnd)
	GuessCount = guessCountOrig - 1
	wrongGuess = True
	while wrongGuess == True:
		print "You have %r guesse(s) left!\n" % (GuessCount + 1)
		time.sleep(.5)
		try:
			guess = raw_input("Take a guess! \n> ")
			time.sleep(.5)
			guess = int(guess)
			if guess == num:
				print '\nYou are correct!\n'
				wrongGuess = False
				goagain()
			else:
				if guess > num and GuessCount > 0:
					print "\nYour guess is too high!\n"
					time.sleep(.5)
					GuessCount = GuessCount - 1
				elif guess < num and GuessCount > 0:
					print "\nYour guess is too low!\n"
					time.sleep(.5)
					GuessCount = GuessCount - 1
				else:
					print "\nSorry, you are out of guesses, better luck next time!"
					time.sleep(.5)
					print "\nThe number was: %r\n" % (num)
					wrongGuess = False
					goagain()
		except ValueError:
			print "\nThat is not a valid input!\n"
		
			
def easy():
	print "I'm thinking of a number.....\n"
	time.sleep(3)
	guessEval(15, 1, 50)
	
def medium():
	print "I'm thinking of a number.....\n"
	time.sleep(3)
	guessEval(10, 1, 200)

def hard():
	print "I'm thinking of a number.....\n"
	time.sleep(3)
	guessEval(5, 1, 500)
	
def custom():
	wrongOpt = True
	while wrongOpt == True:
		try:
			custOpt1 = raw_input("\nPlease enter a starting number: \n>")
			custOpt1 = int(custOpt1)
			custOpt2 = raw_input("\nPlease enter an ending number: \n>")
			custOpt2 = int(custOpt2)
			custOpt3 = raw_input("\nPlease enter the number of guesses you wish to recieve: \n>")
			custOpt3 = int(custOpt3)
			wrongOpt == False
			print '\nGood Luck!\n'
			time.sleep(3)
			guessEval(custOpt3, custOpt1, custOpt2)
		except ValueError:
			print "\nThat is not a valid input!\n"


def main():
	diffOpt = raw_input("> ")
	if diffOpt == '1':
		print '\nGood Luck!\n'
		easy()
	elif diffOpt == '2':
		print '\nGood Luck!\n'
		medium()
	elif diffOpt == '3':
		print '\nGood Luck!\n'
		hard()
	elif diffOpt == '4':
		custom()
	else:
		print "\nThat is not a valid option!\n"
		main()
		
		
		
		
print """Welcome to Toz's 'Guess my number' Game!

To Play, please select a game option by typing the number 

of the option you would like to select:

1) Easy (1-50)
2) Medium (1-200)
3) Hard (1-500)
4) Custom
"""
main()
