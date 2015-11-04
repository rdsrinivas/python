#!/usr/local/bin/python

# Print the return value of a function

def using_control_once():
    if ( 25 > 15):
        return "Success #1"

def using_control_again():
    if ( not False):
        return "Success #2"

print using_control_once()
print using_control_again()

# Send a parameter to function and print the return value

def greater_less_equal_5(answer):
    if (answer > 5):
        return 1
    elif (answer < 5):         
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

# Print the return value of a called function

def the_flying_circus():
    # Start coding here!
    medium_number = int(raw_input("Enter a number: "))
    if (medium_number > 1) and ( medium_number < 10):
        return True
    elif (medium_number < 1) or (medium_number > 10):
        return False
    else :
        return "Input not a number"
        
        
print the_flying_circus()        
    
