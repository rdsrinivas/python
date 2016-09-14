#!/usr/local/bin/python

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

"""
Add a method, description, to your Animal class. Using two separate print statements, it should print out the name and age of the animal it's called on. Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.
"""

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!

    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Brown",10)
print hippo.description()

"""

    After line 3, add a second member variable called health that contains the string "good".
    Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)
    Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.

"""

ass Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!

    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Brown",10)
print hippo.description()

sloth = Animal("Slow", 3)
ocelot = Animal("Blue", 5)

print hippo.health
print sloth.health
print ocelot.health

