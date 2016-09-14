#!/usr/local/bin/python

""" This program calculates the area of a given shape as selected by the user, either a circle or triange"""

from math import pi
from time import sleep
from datetime import datetime
from datetime import time

now = datetime.now()
print "Calculator is all set to begin \n"
print '%s/%s/%s %s:%s' % (now.month,now.day,now.year, now.hour, now.minute)
sleep(1)

hint="Don't forget to include the correct units! \n"
option = raw_input("Choose Circle(C), Triangle(T), Square(S), or Rectangle(R) ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Input radius of circle : "))
  area = pi * radius ** 2
  print "The pie is baking \n"
  sleep(1)
  print ("Area is %.2f \n %s" % (area, hint))
  
elif option == "T":
  base = float(raw_input("Input base of triangle : "))
  height = float(raw_input("Input height of triangle : "))
  area = 0.5 * base * height
  print "Uni Bi Tri...\n"
  sleep(1)
  print ("Area is %.2f \n %s" % (area, hint))

elif option == "S":
  side = float(raw_input("Input side of square : "))
  area = side ** 2
  print "Uni Bi Tri Square ...\n"
  sleep(1)
  print ("Area is %.2f \n %s" % (area, hint))
  
elif option == "R":
  side1 = float(raw_input("Input side 1 of Rectangle : "))
  side2 = float(raw_input("Input side 2 of Rectangle : "))
  area = side1 * side2
  print "Uni Bi Tri Square ...\n"
  sleep(1)
  print ("Area is %.2f \n %s" % (area, hint)) 
  
else:
  print ("Entered neither C nor T, exiting...\n")
  
  
