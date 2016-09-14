#!/usr/local/bin/python
"""

Reversing a List

We have seen that a positive stride progresses through the list from left to right.

A negative stride progresses through the list from right to left.

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]

In the example above, we print out ['E', 'D', 'C', 'B', 'A'].
Instructions

    Create a variable called backwards and set it equal to the reversed version of my_list.
    Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.


"""
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
