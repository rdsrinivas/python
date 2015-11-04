#!/usr/local/bin/python
# Checking out an if-elif statement

def clinic():
	print "You've just entered the clinic !"
	print "Do you take the door on the right or the left?"
	answer = raw_input("Type left of right and hit 'Enter'").lower()
	
	if answer == 'left' or answer == 'l':
		print "THis is the Verbal Abuse Room, you heap of parrot droppings!"
	elif answer == 'right' or answer == 'r':
		print "Of course this is The Argument Room, I've told you that already!"
	else:
		print "You didnt pick left or right! Try again."
		clinic()

clinic()
