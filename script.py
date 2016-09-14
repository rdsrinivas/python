#!/usr/local/bin/python

print "Welcome to Python!"

my_int=7
print my_int

def spam():
    eggs = 12
    return eggs

print spam()

cats = 3
spam = True
eggs = False

"""This is a test
blahcadfad
asdf;alkd;fadf
"""

string_1 = "Camelot"
string_2 = "place"

print "Lets not go to %s . 'Tis a silly %s" % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, and your favorite color is %s " % (name, quest, color)


### Function is_even
def is_even():
   x = int(raw_input("Type a number:"))
   print x

   if x % 2 == 0:
      return True
   else:
      return False

status = is_even()

### Function is_int
def is_int(number):
    if number - round(number) == 0:
        return True
    else:
        return False
    
    
number = float(raw_input("Type in a number"))
status = is_int(number)
