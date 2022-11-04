import time
import random
import os

//variables
global playerHp
global playerMoney
global playerInvintory

playerHp = 100
playerMoney = 100
playerInvintory = ["Basic sword", "Leather armour"]

//starting text and warning

print("Created by Ligig games")
print("")
print("Important note: do not move the .exe file out of the folder it came in, as it will make the game unplayable.")
print("You can make a shortcut to acess in quickly!")
print("Loading game...")

//functions

// title screen look and options

def titleScreen():
	print("+=======================================================+")
	print("|                                                       |")
	print("|                    The tale of                        |")
	print("|                      Ellamir                          |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|        Start           load            exit           |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("|                                                       |")
	print("+=======================================================+")

def titleScreenDecision():
	answer = input()

	if answer.lower().strip() == 'exit':
		print("See you next time!")

	elif answer.lower().strip() == 'load':
		print("Sorry, I have not made that feature yet...")
		titleScreenDecision()

	elif answer.lower().strip() == 'start':
		print("Let the game begin...")
		intro()

// start of the game text

def intro():
	print("")