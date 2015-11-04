#!/usr/local/bin/python

ui = raw_input("What is 1 + 1? > ")
def the_flying_circus():
    if ui == 2:
        print "Yes"
    elif ui < 2 or ui > 2:
        print "No"
    else:
        print "Try Again"
    return True
