#!/usr/local/bin/python

def factorial(x):
    result = x
    while x > 1:
        result = result*(x-1)
        x-= 1
    return result




number = int(raw_input("Type in an integer"))
print factorial(number)
