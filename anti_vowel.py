#!/usr/local/bin/python

"""
anti_vowel

Nice work. Next up: vowels!
Instructions

Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

    Don't count Y as a vowel.
    Make sure to remove lowercase and uppercase vowels.

"""

def anti_vowel(text):
    k=len(text)
    newtext=[]
    for i in range(k):
        if text[i] not in ('a','A','e','E','i','I','o','O','u','U'):
            newtext.append(text[i])
#            let=""
#        else:
#            newtext.append(text[i])
    
    return "".join(newtext)
    
word=raw_input("Type in a string :")
print "The word stripped of vowels is: " + anti_vowel(word)
