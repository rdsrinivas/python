#!/usr/local/bin/python

"""This is madlibs story with blank spaces to be filled in by the reader using their own words"""

print "Hello! This is the Mad Libs program"
name = raw_input("Please input a name  : ")

print "We now need three desciptive adjectives"
adject1 = raw_input("Input adjective 1 : ")
adject2 = raw_input("Input adjective 2 : ")
adject3 = raw_input("Input adjective 3 : ")

print "And now for three verbs"
verb1 = raw_input("Input verb 1 : ")
verb2 = raw_input("Input verb 2 : ")
verb3 = raw_input("Input verb 3 : ")

print "Please type in four nouns"
noun1 = raw_input("Input noun 1 : ")
noun2 = raw_input("Input noun 2 : ")
noun3 = raw_input("Input noun 3 : ")
noun4 = raw_input("Input noun 4 : ")

print "And now please provide the following"
animal = raw_input("Name of an animal : ")
food = raw_input("Name of a food article : ")
fruit = raw_input("Name a fruit : ")
number = raw_input("Input a number : ")
superhero = raw_input("Type in a superhero : ")
country = raw_input("Name a country : ")
dessert = raw_input("your favorite dessert : ")
year = raw_input("type in a year : ")


#The template for the story
"""STORY = "This morning I woke up and felt %s because _ was going to finally %s over the big _ %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to _ to the rythym of the %s, which made all of the %ss very _. %s tried to _ into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping _ into a puddle of %s. %s then fell asleep and woke up in the year _, in a world where %ss ruled the world."
"""
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adject1, name, verb1, adject2, noun1, noun2, animal, food, verb2, noun3, fruit, adject3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)

#STORY = "Just one adjective %s"
#print STORY % (adject1)
