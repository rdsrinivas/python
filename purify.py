#!/usr/local/bin/python


"""
purify

Awesome! Now let's practice filtering a list.
Instructions

Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.

For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
"""

def purify (n):
   return [x for x in n if x%2 == 0]
   
print purify([1,2,3,4,5])

""" OR """

def purify(numlist):
    newlist = []
    for i in numlist:
        if i % 2 == 0 :
            newlist.append(i)
            
    return newlist
    
print purify([1,2,3,4,5,6,7,8,9,10,4,5,6,7,8,9,10,4,5,6,7,8,9,10,4,5,6,7,8,9,10])
