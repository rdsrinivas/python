#!/usr/local/bin/python

def is_int(number):
    if number - round(number) == 0:
        return True
    else:
        return False
    
    
number = float(raw_input("Type in a number"))
status = is_int(number)
