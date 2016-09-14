#!/usr/local/bin/python

# Slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# Add code below!
bitlist = [ x for x in my_list[::] if x %2 != 0 ]
print bitlist
