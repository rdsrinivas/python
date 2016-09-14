#!/usr/local/bin/python

def cube (n):
    thecube=n**3
    print  n, thecube
    return thecube
    
#cube (3)

def by_three(a):
    if (a % 3 == 0) :
        return cube(a)
    else:
        return False
        
    
for x in range (1, 100):
    by_three(x)
