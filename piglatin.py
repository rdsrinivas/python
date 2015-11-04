#!/usr/local/bin/python

"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word=word[1:len(word)]
    if first in ['a', 'e', 'i', 'o', 'u']:
        print 'Vowel'
        new_word = word[1:len(word)] + first + pyg
        print new_word
    else:
        print 'Consonant'
        word_length = len(word)
        new_word = word[1:word_length] + first + pyg
        print new_word
        
else:
    print 'empty'
