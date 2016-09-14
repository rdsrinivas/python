#!/usr/local/bin/python

"""

is_prime

A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (Boy, that's a mouthful.)

In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.

If there is a number between 1 and x that goes in evenly, then x is not prime.
Instructions

    Define a function called is_prime that takes a number x as input.
    For each number n from 2 to x - 1, test if x is evenly divisible by n.
    If it is, return False.
    If none of them are, then return True.
"""

# Hint: Need to convert string into array, array back to string. Return string
def reverse(text):
    rstring=[]
    k = len(text)
    for i in range(k):
        rstring.append(text[k-(i+1)])
    return "".join(rstring)
    
string = raw_input("Type in a string: ")
print "The string is" + string
print "The reverse string is " + reverse(string)
