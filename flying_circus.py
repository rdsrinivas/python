#!/usr/local/bin/python

def the_flying_circus():
    # Start coding here!
    answer = int(raw_input("Guess the answer :")
    if answer < 20 or answer > 30:
        print "you are not close"
        return True

    elif ( answer >= 20 ) and ( answer <= 24 ):
        print "You are a little low!"
        return True
    
    elif ( answer >=26 ) and ( answer <= 30 ):
        print "you are a little high"
        return True
    
    else:
        print "You are just right!"
        return True
  
the_flying_circus()
