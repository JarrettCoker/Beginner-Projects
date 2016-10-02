# Dice Rolling Simulator
# Python 2.7.10
# Written by Oddjob922

import time
import random
print "Welcome to Toz's dice rolling simulator!\n"

def goagain():
	print "Would you like to roll again? [Y/N]\n"
	againchoice = raw_input("> ")
	if againchoice == 'y' or againchoice == 'Y':
		start()
	elif againchoice == 'n' or againchoice == 'N':
		exit()
	else:
		print "That is not a valid choice!\n"
		goagain()


def roller1():
	print "\nRolling....."
	time.sleep(2)
	print "\nYour number is:\n\n%r\n" % (random.randrange(1, 7))
	time.sleep(1)
	goagain()


def roller2():
	print "\nRolling....."
	time.sleep(2)
	print "\nYour first number is:\n\n%r\n" % (random.randrange(1, 7))
	time.sleep(2)
	print "\nYour second number is:\n\n%r\n" % (random.randrange(1, 7))
	time.sleep(1)
	goagain()


def start():
	print "Enter the number of the choice you wish to select:"
	print "\n1) Single die"
	print "\n2) Two dice"
	startchoice = raw_input("\n> ")
	if startchoice == '1':
		roller1()
	elif startchoice== '2':
		roller2()
	else:
		print "That is not a valid choice!\n"
		start()

start()	
	
	
