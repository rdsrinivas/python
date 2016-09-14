#!/usr/local/bin/python


"""In this project, we'll build a program that rolls a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins."""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number : "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum value possible is : " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "Invalid guess"
    return 
  else:
    print "Rolling...."
    sleep(2)
    print ("First roll is : %d") % first_roll
    sleep(1)
    print ("second roll is : %d") % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result .. : " 
    sleep(1)
    if user_guess > total_roll:
      print "You have won!"
      return
    else:
      print "You have lost!"
      return 

number_of_sides = int(raw_input("Choose no of sides : "))
roll_dice(number_of_sides)
