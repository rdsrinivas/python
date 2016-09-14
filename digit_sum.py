#!/usr/local/bin/python

def digit_sum(x):
    x = str(x)
    sum = 0
    count = 0
    while count < len(x):
        sum = sum + int(x[count])
        count = count + 1
        
    return sum

number = int(raw_input("Type an integer:"))
print  digit_sum(number)

